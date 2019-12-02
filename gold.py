# https://pkgstore.datahub.io/core/gold-prices/102/datapackage.json
#monthly prices
# https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json
# someArray = []
import pandas as pd
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
#===========================================================>
import pymongo
try:
    myClient = pymongo.MongoClient("mongodb://localhost:27017/")
except pymongo.errors.ConnectionFailure as e:
    print(e)
#db name
db = myClient["python3"]
#collection name
col = db["some interest data set"]
#========================= SSL Certificate =====================>
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#===============================Start=======================>
status = 'start'
while(status=='start'):
    import json
    import requests
    # response = requests.get("https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json")
    url = "https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json"
    
    extractedJson = urllib.request.urlopen(url,context=ctx).read()
    df = pd.read_json(extractedJson)
    print(df)
    # print(prices[0])
    # for price in prices:
    #     Date = price["Date"]
    #     Mark = price["Price"]
    #     print(str(Date) + "_" + str(Mark))




