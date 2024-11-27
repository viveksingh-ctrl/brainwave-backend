from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "test_db"
COLLECTION_NAME = "test_collection"

# Initialize MongoDB Client
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Create a document
def create_document(document):
    """Insert a new document into the collection."""
    result = collection.insert_one(document)
    print(f"Document inserted with _id: {result.inserted_id}")
    return result.inserted_id

# Read documents
def read_documents(query=None):
    """
    Read documents from the collection based on a query.
    If no query is provided, fetch all documents.
    """
    query = query or {}
    documents = collection.find(query)
    print("Documents found:")
    for doc in documents:
        print(doc)

# Update a document
def update_document(document_id, updated_fields):
    """
    Update a document in the collection.
    :param document_id: The _id of the document to update.
    :param updated_fields: A dictionary of fields to update.
    """
    result = collection.update_one(
        {"_id": ObjectId(document_id)},
        {"$set": updated_fields}
    )
    if result.modified_count > 0:
        print(f"Document with _id: {document_id} updated successfully.")
    else:
        print(f"No document found with _id: {document_id} or no changes made.")

# Delete a document
def delete_document(document_id):
    """
    Delete a document from the collection by its _id.
    """
    result = collection.delete_one({"_id": ObjectId(document_id)})
    if result.deleted_count > 0:
        print(f"Document with _id: {document_id} deleted successfully.")
    else:
        print(f"No document found with _id: {document_id}.")

# Example Usage
if __name__ == "__main__":
    # Create
    new_document = {"name": "John Doe", "age": 30, "email": "johndoe@example.com"}
    document_id = create_document(new_document)

    # Read
    print("\n--- Reading All Documents ---")
    read_documents()

    # Update
    print("\n--- Updating Document ---")
    updated_fields = {"age": 31}
    update_document(document_id, updated_fields)

    # Read after Update
    print("\n--- Reading Updated Document ---")
    read_documents({"_id": ObjectId(document_id)})

    # Delete
    print("\n--- Deleting Document ---")
    delete_document(document_id)

    # Read after Delete
    print("\n--- Reading All Documents After Deletion ---")
    read_documents()
