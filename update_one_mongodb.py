from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("testguidedb")
    collection = database.get_collection("testdata")

    query_filter = { "Value_one": "30" }
    update_operation = { "$set" : 
        { "Value_one": "40" }
    }
    result = collection.update_one(query_filter, update_operation)

    print(result.modified_count)

    # Query for a movie that has the title 'Back to the Future'
    query = { "Value_one": "40" }
    data = collection.find_one(query)
    print(data)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
