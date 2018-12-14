# coding: utf-8
# __author__: ""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tornado.options import options
import contextlib
from tornado import concurrent, gen
import time


class db(object):
    DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8'.format(**options.conf.db)
    engine = create_engine(DB_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base((engine))

    def __init__(self):
        pass

    # 将创建好的User类，映射到数据库的users表中
    @staticmethod
    def init_db(self):
        print('------------create_all-------------')
        self.Base.metadata.create_all(self.engine)
        print('------------create_end-------------')

    @contextlib.contextmanager
    def query(self):
        pass

    # @concurrent.run_on_executor
    # def asyn_query(self):
    #     t = time.time()
    #     db = client.conn()
    #     db.execute('''select * from TABLE_CONSTRAINTS join (CHARACTER_SETS,STATISTICS)''')
    #     db.close()
    #     return time.time() - t
    #
    # @gen.coroutine
    # def get(self, *args, **kwargs):
    #     # print self.get_query_argument("test11")
    #     time = yield self.asyn_query
    #     print(time)
    #     self.write(time)
    #     print("over")
    #
    #     self.finish()

if __name__ == "__main__":
    db.init_db()



