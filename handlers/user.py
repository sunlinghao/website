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
            self.render("user.html",users = user)  #user是一个字典
        # user = user_infos[0]
        # self.render("user.html", users=user)

    def post(self):
        value = self.get_argument("value")
        #count = mrd.select_item_count('mysina_db','tec','text',value)
        corsur = mrd.select_item('mysina_db','tec','text',value)
        # print type(corsur)
        if corsur:
            items = []
            for item in corsur:
            #print item
                items.append(item)
            #json.dumps : dict转成str
            n_str = json.dumps(items,ensure_ascii=False)
            fp = open("templates/1.json", 'w')
            fp.write(n_str)
            fp.close()
            # self.write(n_str)
        #查询无结果时
        else:
            fp = open("templates/1.json", 'w')
            fp.write('[{"text":""}]')
            fp.close()




class JsonHandler(tornado.web.RequestHandler):

    def get(self):
        self.clear()
        fp = open("templates/1.json", 'r')
        fstr = fp.read()
        fp.close()
        #self.render("1.json")  # 向请求者返回网页模板  只能使用一次
        self.write(fstr)

