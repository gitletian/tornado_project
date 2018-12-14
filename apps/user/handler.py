# coding: utf-8
# coding: utf-8
# __author__: ""


from apps.base_handler import BaseHandler
from datetime import datetime
from models.user_model import user_model
from tornado.websocket import WebSocketHandler


class LoginHandler(BaseHandler):
    def get(self):
        self.render("user/login.html", next=self.get_argument("next"))

    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")

        # 根据用户名去查找数据库
        search_user = user_model.by_name(username)
        if search_user and search_user.auth_password(password):
            # 登录成功调用方法
            self.success_login(search_user)
            self.redirect(self.get_argument("name"))
        else:
            self.write(u"登录失败")

    # 登录成功附加别的属性
    def success_login(self, user):
        user.last_login = datetime.now()
        user.loginnum += 1
        self.db.add(user)
        self.db.commit()
        self.session.set('username', user.user_name)


class RegisterHandler(BaseHandler):
    def get(self):
        # self.render("user/register.html")
        self.render("user/count_user.html")

    def post(self):
        username = self.get_argument("name", "")
        password = self.get_argument("pass", "")
        if not username and not password:
            self.write(u"用户名或密码输入有错误")

        # 先查询数据库是否已经存在该用户
        search_name = user_model.by_name(username)
        if search_name:
            self.write(u"该用户名已经存在，不能重复注册")
        else:
            user = user_model()
            user.user_name = username
            user.password = password
            self.db.add(user)
            self.db.commit()
            self.write(u"注册成功")


class CountUserHandler(WebSocketHandler):

    users = set()  # 用来存放在线用户的容器

    def open(self, *args, **kwargs):
        self.users.add(self)  # 建立连接后添加用户到容器中
        for u in self.users:
            u.write_message(u"[%s]-[%s]-进入" % (self.request.remote_ip, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def on_message(self, message):
        for u in self.users:  # 向在线用户广播消息
            u.write_message(
                u"[%s]-[%s]-进入" % (self.request.remote_ip, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            print("=================", len(self.users))

    def on_close(self):
        self.users.remove(self)  # 用户关闭连接后从容器中移除用户
        for u in self.users:
            u.write_message(
                u"[%s]-[%s]-离开" % (self.request.remote_ip, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def check_origin(self, origin):
        return True

