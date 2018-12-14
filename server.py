# coding: utf-8
# __author__: ""

from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options
from application import application as app
from utils.db import db


if __name__ == "__main__":
    options.parse_command_line()

    if options.t:
        db.init_db()

    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('start server...')
    IOLoop.instance().start()


