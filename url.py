# coding: utf-8
# __author__: ""

import tornado.web
from apps.main.handler import MainHandler
from apps.user.handler import LoginHandler
from apps.user.handler import RegisterHandler, CountUserHandler


url = [
    (r'/', MainHandler),
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler),
    (r"/count_user", CountUserHandler),

    (r"/upload/(.*)", tornado.web.StaticFileHandler, {"path": "upload"}),  # 这是上传的静态文件，用自定义静态文件的路由。
]

