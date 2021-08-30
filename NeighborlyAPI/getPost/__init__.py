import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://gerke01:bTZD4o82VRhdB974z34mf4TBCQbzB34D3VcFUTRP5myLGBkL3OnLbubm4ZIorLGemElbk8Pq7t1DQRPkLPUpCg==@gerke01.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@gerke01@"
            client = pymongo.MongoClient(url)
            database = client['gerke01']
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
