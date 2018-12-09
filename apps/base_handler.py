# coding: utf-8
# __author__: ""

from pycket.session import SessionMixin
import tornado.websocket
import tornado.web
from pycket.session import SessionMixin
from utils.db import db
from models.user_model import user_model


class BaseHandler(tornado.web.RequestHandler, SessionMixin):
    def initialize(self):
        self.db = db.session

    def get_current_user(self):
        if self.session.get("username"):
            return user_model.by_name(self.session.get("username"))
        else:
            return None

    def on_finish(self):
        self.db.close()


class BaseWebSocket(tornado.websocket.WebSocketHandler, SessionMixin):
    def get_current_user(self):
        if self.session.get("username"):
            return user_model.by_name(self.session.get("username"))
        else:
            return None