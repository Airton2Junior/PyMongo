#https://www.mongodb.com/pt-br/docs/languages/python/pymongo-driver/current/write-operations/#std-label-pymongo-write

import pymongo
from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("testguidedb")
    collection = database.get_collection("testdata")

    operations = [
        pymongo.InsertOne(
            {
                "<field name>" : "<value>"
            }
        ),
        pymongo.UpdateMany(
            { "<field to match>" : "<value to match>" },
            { "$set" : { "<field name>" : "<value>" }},
        ),
        pymongo.DeleteOne(
            { "<field to match>" : "<value to match>" }
        ),
    ]

    result = collection.bulk_write(operations)

    print(result)

except Exception as e:
    raise Exception("The following error occurred: ", e)

