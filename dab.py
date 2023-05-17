from pymongo import MongoClient


mongo_url = "mongodb://localhost:27017"
mongo_db = MongoClient(mongo_url)

db = mongo_db["newdatabase"]