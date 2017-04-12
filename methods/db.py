# coding:utf-8

import pymongo

client = pymongo.MongoClient('localhost',27017)
db = client['mydb']
test = db['test']
# dic = {"username":"hahaha","password":"222"}
# test.insert(dic)