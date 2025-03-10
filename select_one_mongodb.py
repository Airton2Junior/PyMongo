from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("testguidedb")
    testedata = database.get_collection("testdata")

    # Query for a movie that has the title 'Back to the Future'
    query = { "Value_one": "30" }
    data = testedata.find_one(query)

    print(data)

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
