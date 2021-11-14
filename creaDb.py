import pymongo
from pymongo import MongoClient

# connection
client = MongoClient('localhost', 27017)

# create db
db = client.testdb

# create a collection
users_collection = db.users

users_collection.create_index([("firstname", pymongo.ASCENDING)])
users_collection.create_index([("lastname", pymongo.ASCENDING)])
users_collection.create_index([("devices", pymongo.ASCENDING)])

# create documents
p1 = {"firstname": "Mario", "lastname": "Rossi", "age": 30, "devices": ["tizen", "iphone"]}
p2 = {"firstname": "Giuseppe", "lastname": "Verdi", "age": 70, "devices": ["apple"]}

# insert documents
users_collection.insert_one(p1)
users_collection.insert_one(p2)

