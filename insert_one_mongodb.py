import pymongo
from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("testguidedb")
    collection = database.get_collection("testdata")

    result = collection.insert_one({ "Value_one" : "40" })

    print(result.acknowledged)
    
    client.close()

except Exception as e:
    raise Exception("The following error occurred: ", e)

