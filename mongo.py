# from adapter import MongoDBAdapter

# adapter = MongoDBAdapter('mongodb://localhost:27017', 'database')
# adapter.connect()

# document = {'name': 'Hardy', 'gender': 'Male'}
# collection_name = 'table'
# result = adapter.insert_document(collection_name, document)

# print(f"Inserted document with ID: {result}")

# from adapter import MongoDBAdapter

# adapter = MongoDBAdapter('mongodb://localhost:27017', 'database')
# adapter.connect()

# # insert a new person
# document = {'name': 'Hardy', 'gender': 'Male'}
# collection_name = 'table'
# result = adapter.insert_document(collection_name, document)
# print(f"Inserted document with ID: {result}")

# # insert another person
# document = {'name': 'Alice', 'gender': 'Female'}
# collection_name = 'table'
# result = adapter.insert_document(collection_name, document)
# print(f"Inserted document with ID: {result}")

# # insert multiple people at once
# documents = [
#     {'name': 'Bob', 'gender': 'Male'},
#     {'name': 'Charlie', 'gender': 'Male'},
#     {'name': 'Eve', 'gender': 'Female'}
# ]
# collection_name = 'table'
# result = adapter.insert_document(collection_name, documents)
# print(f"Inserted {len(result.inserted_ids)} documents")

# from adapter import MongoDBAdapter

# adapter = MongoDBAdapter('mongodb://localhost:27017', 'database')
# adapter.connect()

# document1 = {'name': 'Hardy', 'gender': 'Male'}
# collection_name = 'table'
# result1 = adapter.insert_document(collection_name, document1)
# print(f"Inserted document with ID: {result1}")

# document2 = {'name': 'Lucy', 'gender': 'Female'}
# result2 = adapter.insert_document(collection_name, document2)
# print(f"Inserted document with ID: {result2}")

# document3 = {'name': 'John', 'gender': 'Male', 'age': 30}
# result3 = adapter.insert_document(collection_name, document3)
# print(f"Inserted document with ID: {result3}")



# adapter = MongoDBAdapter('mongodb://localhost:27017', 'database')
# adapter.connect()

# collection_name = 'table'

# document1 = {'name': 'Hardy', 'gender': 'Male'}
# result1 = adapter.insert_document(collection_name, document1)
# print(f"Inserted document with ID: {result1}")

# document2 = {'name': 'Lucy', 'gender': 'Female'}
# result2 = adapter.insert_document(collection_name, document2)
# print(f"Inserted document with ID: {result2}")

# document3 = {'name': 'John', 'gender': 'Male', 'age': 30}
# result3 = adapter.insert_document(collection_name, document3)
# print(f"Inserted document with ID: {result3}")

# adapter.disconnect()
# from adapter import MongoDBAdapter
# adapter = MongoDBAdapter('mongodb://localhost:27017', 'database')
# adapter.connect()
# collection_name ='table'
# document1 = {'name': 'Hardy', 'gender': 'Male'}
# result1 = adapter.insert_document(collection_name, document1)
# print(f"Inserted document with ID: {result1}")

# document2 = {'name': 'Lucy', 'gender': 'Female'}
# result2 = adapter.insert_document(collection_name, document2)
# print(f"Inserted document with ID: {result2}")

# document3 = {'name': 'John', 'gender': 'Male', 'age': 30}
# result3 = adapter.insert_document(collection_name, document3)
# print(f"Inserted document with ID: {result3}")

# adapter.disconnect()


from adapter import MongoDBAdapter
mongo_url = "mongodb://localhost:27017"
db_name = "database"
collection_name = "table"

# Connect to the database
adapter = MongoDBAdapter(mongo_url, db_name)
adapter.connect()

# Check if the collection exists, if not, create it
if collection_name not in adapter.db.list_collection_names():
    adapter.db.create_collection(collection_name)

# Define the documents to be inserted
documents = [
    {'name': 'Hardy', 'gender': 'Male'},
    {'name': 'Lucy', 'gender': 'Female'},
    {'name': 'John', 'gender': 'Male', 'age': 30},
    {'name':'musi','gender':'Female'}
]

# Insert the documents into the collection
result = adapter.insert_documents(collection_name, documents)
print(f"Inserted documents with IDs: {result}")

# Disconnect from the database
adapter.disconnect()