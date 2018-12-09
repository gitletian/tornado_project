# coding: utf-8
# __author__: ""

from tornado.options import define
import tornado.web
from url import url
from conf import settings


def application_handle(handler=[]):
    # 定义一个默认的端口
    define("port", default=settings["port"], help="run port ", type=int)
    define("t", default=False, help="creat tables", type=bool)

    # 加入静态文件的直接访问。
    handler.append((r"/upload/(.*)", tornado.web.StaticFileHandler, {"path": "upload"}))  # 这是上传的静态文件，用自定义静态文件的路由。

    # 加载 url
    handler.extend(url)

    return handler


handlers = application_handle()
application = tornado.web.Application(
    handlers=handlers,
    **settings
)


