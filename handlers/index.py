# coding:utf-8

import tornado.web
import methods.readdb as mrd

class IndexHandler(tornado.web.RequestHandler):
    """
    请求-处理程序类  Handler
    """
    def get(self):
        one_user = mrd.select_one_user("username")

        self.render("index.html",user=one_user)  # 向请求者返回网页模板

    def post(self):
        username = self.get_argument("username")# 从data中选择数据
        password = self.get_argument("password")
        # self.write(username)
        user_infos = mrd.select_collection('username',username) # user_infos是一个列表

        if user_infos:
            doc = user_infos[0]
            db_pwd = doc["password"]
            if db_pwd == password:
                self.write(username)   #data

            else:
                self.write("your password was not right.")

        else:
            self.write("There is no this user.")
