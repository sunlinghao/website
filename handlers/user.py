# coding:utf-8

import tornado.web
import methods.readdb as mrd
import json

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("user")  # 获取url中参数
        user_infos = mrd.select_collection("username",username)
        if user_infos:
            user = user_infos[0]
            self.render("user.html",users = user)
        # user = user_infos[0]
        # self.render("user.html", users=user)

    def post(self):
        print "post"
        count = mrd.select_item_count('mysina_db','tec','text','sz')
        corsur = mrd.select_item('mysina_db','tec','text','sz')
        # print type(corsur)
        items = []
        for item in corsur:
            #print item
            items.append(item)
        print type(items)   #json.dumps : dict转成str
        n_str = json.dumps(items,ensure_ascii=False)
        n_json = json.loads(n_str)
        self.write({"json":n_json})
