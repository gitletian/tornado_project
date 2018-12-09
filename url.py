# coding: utf-8
# __author__: ""

from apps.main.handler import MainHandler
from apps.user.handler import LoginHandler
from apps.user.handler import RegisterHandler


url = [
    (r'/', MainHandler),
    (r"/login", LoginHandler),
    (r"/register", RegisterHandler)
]

