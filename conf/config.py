# coding: utf-8
# __author__: ""


dev = dict(
    debug=True,  # 设置debug启动方式
    port=8000,
    template_path="templates",  # 设置模板路径
    static_path="static",  # 设置静态文件路径
    login_url="/login",  # 重定向到登录页面
    # packet的配置
    pycket={
        "engine": "redis",  # 配置存储类型
        "storage": {
            "host": "172.16.1.100",
            "port": 6379,
            "db_sessions": 5,
            "db_notifications": 11,
            "max_connections": 2 ** 31
        },
        "cookies": {
            "expires_days": 30,
            "max_age": 360
        }
    },
    cookie_secret="aaa",
    xscf_cookies=True,
    db=dict(
        host='172.16.1.100',
        port=3306,
        database='tornado',
        username='tornado',
        password='123456',
    )
)


aut = dict(


)


pro = dict(


)

