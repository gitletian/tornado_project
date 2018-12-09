# coding: utf-8
# __author__: ""

import tornado.ioloop
import tornado.httpserver
from tornado.options import options
# from .application import application as app
import application as app
from utils.db import db


if __name__ == "__main__":
    options.parse_command_line()

    if options.t:
        db.init_db()

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print('start server...')
    tornado.ioloop.IOLoop.instance().start()


