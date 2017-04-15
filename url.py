# coding:utf-8
"""
the url structure of website
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.user import JsonHandler

url = [(r'/',IndexHandler),#访问根目录 交给IndexHandler类get()方法处理
       (r'/user',UserHandler),
       (r'/1.json',JsonHandler)
       ]
# url = [(r'/',UserHandler),#访问根目录 交给IndexHandler类get()方法处理
#        ]