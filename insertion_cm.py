from pymongo import MongoClient
import json

from extras import BLOG_CONTENT_TYPE 

DB_2 = 'TEST_CM'
COLLECTION_NAME_2 = 'TEST'
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db2 = client[DB_2]
c2 = db2[COLLECTION_NAME_2]

c2.insert_one(document = BLOG_CONTENT_TYPE)