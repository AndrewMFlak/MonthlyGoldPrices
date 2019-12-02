# https://pkgstore.datahub.io/core/gold-prices/102/datapackage.json
#monthly prices
# https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json
# someArray = []
print('hello world')
count = 0
start = True
#===========================================================>
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
#===========================================================>
import json
import requests
response = requests.get("https://pkgstore.datahub.io/core/gold-prices/monthly_json/data/40d9ba25a853b99b805eef645852cd35/monthly_json.json")
prices = json.loads(response.text)
print(prices[0])
for price in prices:
    Date = price["Date"]
    Mark = price["Price"]
    print(str(Date) + "_" + str(Mark))




