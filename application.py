# coding:utf-8

"""
build
"""
from url import url
import tornado.web
import os

settings = dict(template_path = os.path.join(os.path.dirname(__file__),"templates"),# 指定模板路径
               static_path = os.path.join(os.path.dirname(__file__),"statics"), # 指定js路径
               )
application = tornado.web.Application(
    handlers = url,
    **settings
)