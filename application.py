# coding: utf-8
# __author__: ""

import tornado.web
from tornado.options import define
from conf.config import conf
from utils.object_dict import ObjectDict

# 定义一个默认的端口
define("port", default=conf.port, help="run port ", type=int)
define("t", default=None, help="creat tables", type=bool)
define("conf", default=conf, help="dict object", type=ObjectDict)


from url import url
application = tornado.web.Application(
    handlers=url,
    **conf
)





