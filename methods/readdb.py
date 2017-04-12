# coding:utf-8

from db import *

def select_collection(condition,value):
    count = test.find({condition:value}).count()
    if count==0:
        return None
    cursor = test.find({condition:value})
    return cursor


def select_one_user(condition):
    count = test.find({},{condition:1}).count()
    if count == 0:
        return None
    cursor = test.find({},{condition:1})
    one_user = cursor[0]["username"]
    return one_user

def select_item_count(db,collection,condition,value):
    db_now = client[db]
    collection_now = db_now[collection]
    count = collection_now.find({condition: {'$regex': '.*{0}.*'.format(value)}}).count()
    return count

def select_item(db,collection,condition,value):
    if select_item_count(db,collection,condition,value)==0:
        return None
    db_now = client[db]
    collection_now = db_now[collection]
    corsur = collection_now.find({condition:{'$regex':'.*{0}.*'.format(value)}},{condition:1,"_id" : 0})
    return corsur