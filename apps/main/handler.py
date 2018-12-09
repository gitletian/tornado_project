# coding: utf-8
# __author__: ""

import tornado.web
from apps.base_handler import BaseHandler


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        print("=========================")
        self.render("main/index.html")




