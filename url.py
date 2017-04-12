# coding:utf-8
"""
the url structure of website
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handlers.index import IndexHandler
from handlers.user import UserHandler

url = [(r'/',IndexHandler),#访问根目录 交给IndexHandler类get()方法处理
       (r'/user',UserHandler),
       ]
# url = [(r'/',UserHandler),#访问根目录 交给IndexHandler类get()方法处理
#        ]