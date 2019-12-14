# https://pkgstore.datahub.io/core/gold-prices/102/datapackage.json
#monthly prices
# https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json
# someArray = []
import pandas as pd
from pandas.io.json import json_normalize
import time
import urllib.request
import urllib.parse
from urllib.request import urlopen

#=================== Welcome To the Party ======================>
print('hello world')
count = 0
start = True
status = ''
#========================== .env ===========================>
import os
from os.path import join, dirname
import dotenv
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
#=========================== MATPLOTLIB ========================>

import matplotlib.pyplot as plt

#======================== PYMONGO =============================>
import pymongo
try:
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
except pymongo.errors.ConnectionFailure as e:
    print(e)
#db name
my_df = ''
db = myClient["python3"]
#collection name
col = db['someInterestingDataSet']
server = 'localhost'
mongoPort = 27017
chunkSize = 1000
#========================= SSL Certificate =====================>
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#========================= Function Declaration =========================>
def write_df_to_mongoDB(
    my_df = my_df,\
    database_name = 'python3',\
    collection_name = 'someInterestingDataSet',\
    server = 'localHost',\
    mongodb_port = 27017,\
    chunk_size = 1000
    ):
    col.create_index("_id")
    my_df.set_index('Date')
    my_list = my_df.to_dict('records')
    for item in my_list:
        try:
            # db.someInterestingDataSet.update_one({'_id':item['Date']},{'$set':item},upsert=True)
            db.someInterestingDataSet.insert_one(item)
            print(item)

        except pymongo.errors.ConnectionFailure as e:
            print("Upsert_OneError",e)

#======================== Flask API =================================>
# from flask import Flask
# from flask import request
# from bson.json_util import dumps
# import json

# app = Flask(__name__)

# @app.route("/gold", methods = ['POST'])
# def add_contact():
#     try:
#         data = json.loads(request.data)
#     except Exception as e:
#         return dumps({'error' : str(e)})

# # running REST interface, port=5000 for direct test
# if __name__ == "__main__":
#     app.run(debug=False, host='0.0.0.0', port=5000)
#========================== Workflow Start ==========================>
status = 'start'
while(status=='start'):
    import json
    import requests
    # response = requests.get("https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json")
    baseUrl = ""
    url = "https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json"
    
    extractedJson = urllib.request.urlopen(url,context=ctx).read()
    data = pd.read_json(extractedJson)
    # json_normalize(data['Date'])
    print(data)
        #  pd.normalize_json.load(extractedJson)
    # my_df = pd.read_json(extractedJson)
    # for someitem in my_df:
    #     print(someitem)
    
    # write_df_to_mongoDB(my_df)
    status = 'stop'
