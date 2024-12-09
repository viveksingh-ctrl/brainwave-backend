from fastapi import FastAPI, HTTPException, Header, Request
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from fastapi.responses import StreamingResponse
from extras import RTE_CONTENT
from prompts import GENERATE_FROM_TEMPLATE_V1, GENERATE_RTE, GRAMMAR, SUMMARIZE, BRAINSTORM
import asyncio
from pymongo import MongoClient
import json
from typing import List, Dict
import uuid 
from datetime import datetime
import random
import string
from fastapi.middleware.cors import CORSMiddleware
from llm import ChatGPTLLM
import time

DB_2 = 'TEST_CM'
COLLECTION_NAME_2 = 'TEST'

MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db2 = client[DB_2]
c2 = db2[COLLECTION_NAME_2]

llm = ChatGPTLLM()

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

db2 = client[DB_2]
c2 = db2[COLLECTION_NAME_2]
# Load environment variables from .env
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For frontend development
    allow_credentials=True,  # If you need cookies or authentication
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)


def serialize_document(doc):
    """Convert MongoDB document to JSON serializable format."""
    doc["_id"] = str(doc["_id"])
    return doc


# Define request body structure
class ChatRequest(BaseModel):
    content_type: str
    query: str

# Define a generator function for streaming the response


async def async_streamer(generator):
    try:
        chunk_size = None  
        random_number = str(uuid.uuid4())
        for chunk in generator.iter_content(chunk_size=chunk_size):
            print(chunk, ' bow bow')
            data = chunk.decode("utf-8").split("data: ")
            for dictionary_string in data:
                if dictionary_string == "":
                    continue
                elif dictionary_string.startswith("[DONE]"):
                    pass
                    # response_output = {
                    #     "id": random_number,
                    #     "content": "[DONE]",
                    #     "complete": True,
                    #     "model": model,
                    # }
                    # yield "data: " + json.dumps(response_output) + "\n"
                dictionary_string = dictionary_string.replace("\n", "")
                try:
                    json_data = json.loads(dictionary_string)
                    print(json_data, ' ham yaha aye')
                    if "content" in json_data["choices"][0]["delta"]:
                        # print(json_data["choices"][0]["delta"]["content"])
                        yield json_data["choices"][0]["delta"]["content"]
                        # response_output = {
                        #     "id": random_number,
                        #     "content": json_data["choices"][0]["delta"]["content"],
                        #     "complete": False,
                        #     "model": model,
                        # }
                        # yield "data: " + json.dumps(response_output) + "\n"
                except json.JSONDecodeError as e:
                    continue
            await asyncio.sleep(0.1)
    except asyncio.CancelledError as e:
        print(e, ' billo raani')
        pass

INPUT_ = content_model = {
    "created_at": "2024-05-21T06:53:54.981Z",
    "updated_at": "2024-08-19T08:45:14.809Z",
    "title": "Adwait",
    "uid": "adwait",
    "_version": 5,
    "inbuilt_class": False,
    "schema": [
        {
            "data_type": "text",
            "display_name": "Title",
            "field_metadata": {
                "_default": True,
                "version": 3
            },
            "mandatory": True,
            "uid": "title",
            "unique": True,
            "multiple": False,
            "non_localizable": False,
            "min": 1,
            "max": 50
        },
        {
            "data_type": "text",
            "display_name": "Multi Line Textbox",
            "uid": "multi_line",
            "field_metadata": {
                "description": "",
                "default_value": "",
                "multiline": True,
                "version": 3
            },
            "format": "",
            "error_messages": {
                "format": ""
            },
            "mandatory": False,
            "multiple": False,
            "non_localizable": False,
            "unique": False
        }
    ],
    "last_activity": {},
    "maintain_revisions": True,
    "description": "",
    "DEFAULT_ACL": {
        "others": {
            "read": False,
            "create": False
        },
        "users": [
            {
                "uid": "blt6bcf0337a4f6e8f7",
                "read": True,
                "sub_acl": {
                    "read": True
                }
            }
        ]
    },
    "SYS_ACL": {
        "roles": [
            {
                "uid": "blt0b47d49d8e46ec0f",
                "read": True,
                "sub_acl": {
                    "create": True,
                    "read": True,
                    "update": True,
                    "delete": True,
                    "publish": True
                },
                "update": True,
                "delete": True
            },
            {
                "uid": "blt6ad7a8acd16a5a99",
                "read": True,
                "sub_acl": {
                    "create": True,
                    "read": True,
                    "update": True,
                    "delete": True,
                    "publish": True
                }
            },
            {
                "uid": "blt49c557406956107c",
                "read": True,
                "sub_acl": {
                    "create": True,
                    "read": True,
                    "update": True,
                    "delete": True,
                    "publish": True
                },
                "update": True,
                "delete": True
            }
        ],
        "others": {
            "read": False,
            "create": False,
            "update": False,
            "delete": False,
            "sub_acl": {
                "read": False,
                "create": False,
                "update": False,
                "delete": False,
                "publish": False
            }
        }
    },
    "options": {
        "is_page": False,
        "singleton": True,
        "sub_title": [],
        "title": "title"
    },
    "abilities": {
        "get_one_object": True,
        "get_all_objects": True,
        "create_object": True,
        "update_object": True,
        "delete_object": True,
        "delete_all_objects": True
    },
    "extension_uids": []
}

class TextContent(BaseModel):
    content: str

@app.post('/generate-rte')
async def generate_rte(request: ChatRequest):
    prompt = GENERATE_RTE.format(json_rte = json.dumps(RTE_CONTENT))
    response = llm.answer(query = prompt, model = 'gpt-4o')
    return StreamingResponse(async_streamer(response), media_type="text/plain")

@app.post("/generate-from-template")
async def mapper(request: ChatRequest):
    content_type = request.content_type 
    query = request.query
    # time.sleep(10)
    # prompt = TEMPLATE_RTE.format(content_model = json.dumps(BLOG_CONTENT_TYPE), query = request.message)
    # response = llm.answer(query = prompt, model = 'gpt-4')
    # with open('./content-type.json', 'r') as f:
    #     data = json.load(f)

    prompt = GENERATE_FROM_TEMPLATE_V1.format(content_type = content_type, query = query)
    print(prompt)
    response = llm.answer(query = prompt, model = 'gpt-4-turbo')
    return StreamingResponse(async_streamer(response), media_type="text/plain")    
    # return StreamingResponse(async_streamer(response), media_type="text/plain")

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
async def chat(request: ChatRequest, action = Header('grammar')):
    message = request.message
    with open('./rte_ai.json', 'r') as f:
        data = json.load(f)
    if action == 'summarize':
        prompt = SUMMARIZE.format(input_text = data)
    elif action == 'brainstorm':
        prompt = BRAINSTORM.format(input_text = message, example_json = data)

    elif action == 'grammar':
        prompt = GRAMMAR.format(input_text = data)
    response = llm.answer(query = prompt, model = 'gpt-4-turbo')
    # Check if the message is valid
    return StreamingResponse(async_streamer(response), media_type="text/plain")
@app.get("/templates")
async def create_document(request: Request):
    """Create a new document."""
    result_ = c2.find()
    return [serialize_document(doc) for doc in result_]

@app.post("/templates")
async def create_document(request: Request, item: TextContent):
    """Create a new document."""
    document = json.loads(item.content)
    uid = generate_random_id()
    document['uid'] = uid
    document['last_updated'] = str(datetime.now())
    result_ = c2.insert_one(document = document)
    return [serialize_document(doc) for doc in result_]

@app.post("/content-models")
async def create_document(request: Request, item: TextContent):
    """Create a new document."""
    document = json.loads(item.content)
    uid = generate_random_id()
    document['uid'] = uid
    document['last_updated'] = str(datetime.now())
    c2.insert_one(document)
    result_ = dict(collection.find_one({"uid": uid}))
    result_["_id"] = str(result_["_id"])
    return result_

@app.post("/documents")
async def create_document(request: Request, item: TextContent):
    """Create a new document."""
    document = json.loads(item.content)
    uid = generate_random_id()
    document['uid'] = uid
    document['last_updated'] = str(datetime.now())
    collection.insert_one(document)
    result_ = dict(collection.find_one({"uid": uid}))
    result_["_id"] = str(result_["_id"])
    return result_

@app.get("/documents", response_model=List[dict])
async def read_documents():
    """Read all documents."""
    documents = collection.find().sort("last_updated", -1)
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
    update_data['last_updated'] = str(datetime.now())
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
