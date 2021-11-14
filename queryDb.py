import pymongo
from pymongo import MongoClient

# connection
client = MongoClient('localhost', 27017)

# access to db
db = client.testdb

# access to collection
users_collection = db.users

p = users_collection.find_one()

print(p)

