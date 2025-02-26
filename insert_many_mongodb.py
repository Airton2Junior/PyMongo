import pymongo
from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("testguidedb")
    collection = database.get_collection("testdata")

    document_list = [
        { "Novo Campo" : "Teste" },
        { "Ano" : "2025" }
    ]
    result = collection.insert_many(document_list)

    print(result.acknowledged)
    
    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)

