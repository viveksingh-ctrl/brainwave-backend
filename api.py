from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
from fastapi.responses import StreamingResponse
from prompts import SUMMARIZE, BRAINSTORM
import asyncio
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from typing import List, Dict
import uuid 

import random
import string

def generate_random_id():
    """Generate a 16-character random alphanumeric string starting with 'cs'."""
    prefix = "cs"
    remaining_length = 16 - len(prefix)
    random_part = ''.join(random.choices(string.ascii_letters + string.digits, k=remaining_length))
    return prefix + random_part

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "test_db"
COLLECTION_NAME = "test_collection"

# Initialize MongoDB Client
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]
# Load environment variables from .env
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize Groq client
groq_api_key = os.environ.get("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment")

def serialize_document(doc):
    """Convert MongoDB document to JSON serializable format."""
    doc["_id"] = str(doc["_id"])
    return doc

client = Groq(api_key=groq_api_key)

# Define request body structure
class ChatRequest(BaseModel):
    message: str

# Define a generator function for streaming the response
async def stream_groq_response(message: str, action: str = Header('summarize')):
    try:
        # Create a chat completion request to Groq
        stream = client.chat.completions.create(
            messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": BRAINSTORM.format(input_json=message)},
            ],
            model="llama-3.2-90b-vision-preview",
            temperature=0,
            max_tokens=1024,  # Allow sufficient tokens
            top_p=1,
            stream=True,
        )

        # Stream the incremental responses from the model
        for chunk in stream:
            if chunk.choices[0].delta and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
            else:
                await asyncio.sleep(0.1)  # Pause to simulate streaming behavior

    except Exception as e:
        yield f"Error: {str(e)}"


message_ = {
            "type": "doc",
            "attrs": {},
            "uid": "ee8eb5ce962c4bdbb055561fae985982",
            "children": [
                {
                    "type": "p",
                    "attrs": {},
                    "uid": "1c1bb407a65c4b1f8db1af577a5c5cba",
                    "children": [
                        {
                            "text": "A blog post on scale engineering"
                        }
                    ]
                }
            ],
            "_version": 1
        }
# Define the FastAPI endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    message = request.message

    # Check if the message is valid
    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Return a streaming response
    return StreamingResponse(stream_groq_response(message_), media_type="text/plain")

class TextContent(BaseModel):
    content: str


@app.post("/documents")
async def create_document(request: Request, item: TextContent):
    """Create a new document."""
    document = json.loads(item.content)
    uid = generate_random_id()
    document['uid'] = uid
    collection.insert_one(document)
    result_ = dict(collection.find_one({"uid": uid}))
    result_["_id"] = str(result_["_id"])
    return json.dumps(result_)

@app.get("/documents", response_model=List[dict])
async def read_documents():
    """Read all documents."""
    documents = collection.find()
    return [serialize_document(doc) for doc in documents]


@app.get("/documents/{uid}")
async def read_document(uid: str):
    """Read a document by ID."""
    doc = collection.find_one({"uid": uid})
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return serialize_document(doc)

@app.put("/documents/{uid}")
async def update_document(uid: str, updated_fields: TextContent):
    """Update a document by ID."""
    updated_fields = json.loads(updated_fields.content)
    update_data = {k: v for k, v in updated_fields.items() if v is not None}
    result = collection.update_one(
        {"uid": uid},
        {"$set": update_data}
    )
    doc = collection.find_one({'uid': uid})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    return serialize_document(doc)

@app.delete("/documents/{uid}")
async def delete_document(uid: str):
    """Delete a document by ID."""
    result = collection.delete_one({"uid": uid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"message": "Document deleted"}
