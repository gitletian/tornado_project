#coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 连接数据库的数据
HOSTNAME = '172.16.1.100'
PORT = '3306'
DATABASE = 'tornado'
USERNAME = 'tornado'
PASSWORD = '123456'
# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,
                                                              PASSWORD,
                                                              HOSTNAME,
                                                              PORT,
                                                              DATABASE
                                                              )

# engine
engine = create_engine(DB_URI, echo=False )
# sessionmaker生成一个session类
Session = sessionmaker(bind=engine)
dbSession = Session()
Base = declarative_base(engine)


