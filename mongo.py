import pymongo

def connect_to_mongodb():
    # Replace these with your MongoDB connection details
    client = pymongo.MongoClient("mongodb+srv://abyan:xXKjtyEjckDl6wkD@adara.u7spbca.mongodb.net/?retryWrites=true&w=majority")
    db = client["SAI"]
    return db

def insert_data_to_mongodb(db, data):
    collection = db["stock"]
    collection.insert_one(data)
