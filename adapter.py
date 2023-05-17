# from pymongo import MongoClient




# mongo_url = "mongodb://localhost:27017"
# mongo_db = MongoClient(mongo_url)

# db = mongo_db["newdb"]
# coll = db.create_collection("newtb")

# class MongoDBAdapter:
#     def __init__(self, mongo_url, db):
#         self.url = mongo_url
#         self.db_name = db
#         self.client = None
#         self.db = None

#     def connect(self):
#         self.client = MongoClient(self.mongo_url)
#         self.db = self.client[self.db]

#     def disconnect(self):
#         self.client.close()

#     def insert_document(self, TB2, document):
#         collection = self.db[TB2]
#         result = collection.insert_one(document)
#         return result.inserted_id
    
   
# from pymongo import MongoClient



# class MongoDBAdapter:
#     def __init__(self, mongo_url, db):
#         self.url = mongo_url
#         self.db_name = db
#         self.client = None
#         self.db = None

#     def connect(self):
#         self.client = MongoClient(self.url)
#         self.db = self.client[self.db_name]

#     def disconnect(self):
#         self.client.close()

#     def insert_document(self, table, document):
#         collection = self.db[table]
#         result = collection.insert_many(document)
#         return result.inserted_id
# from pymongo import MongoClient
# 
# mongo_url = "mongodb://localhost:27017"
# mongo_db = MongoClient(mongo_url)

# db = mongo_db["database"]
# collection_name = "table"
# if collection_name not in db.list_collection_names():
#     coll = db.create_collection(collection_name)

# class MongoDBAdapter:
#     def __init__(self, mongo_url, db):
#         self.url = mongo_url
#         self.db_name = db
#         self.client = None
#         self.db = None

#     def connect(self):
#         self.client = MongoClient(self.url)
#         self.db = self.client[self.db_name]

#     def disconnect(self):
#         self.client.close()

#     def insert_document(self, table, document):
#         collection = self.db[table]
#         result = collection.insert_one(document)
#         return result.inserted_id
    

from pymongo import MongoClient



class MongoDBAdapter:
    def __init__(self, mongo_url, db):
        self.url = mongo_url
        self.db_name = db
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.url)
        self.db = self.client[self.db_name]

    def disconnect(self):
        self.client.close()

    def insert_documents(self, collection_name, documents):
        collection = self.db[collection_name]
        result = collection.insert_many(documents)
        return result.inserted_ids






