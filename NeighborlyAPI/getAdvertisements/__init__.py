import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://gerke01:bTZD4o82VRhdB974z34mf4TBCQbzB34D3VcFUTRP5myLGBkL3OnLbubm4ZIorLGemElbk8Pq7t1DQRPkLPUpCg==@gerke01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@gerke01@"
        client = pymongo.MongoClient(url)
        database = client['gerke01']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

