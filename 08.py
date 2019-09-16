#!/home/xiezhengdong/.local/bin/python
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column ,String,Integer,Float,Date
from sqlalchemy.ext.declarative import declarative_base
#建立与数据库的连接
engine=create_engine('mysql+pymysql://gua:123456@localhost:3306/dong')
Base=declarative_base(bind=engine)#创建模型的基础类
Session=sessionmaker(bind=engine)#创建会话类
session=Session()
class User(Base):
    __tablename__='usr'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20),nullable=True)
    age=Column(Integer,nullable=True)
    city=Column(String(15),unique=True)
Base.metadata.create_all()
tom=User(name='tom',age=12,city='上海')
jack=User(name='jack',age=19,city='南京')
bob=User(name='bob',age=20,city='苏州')
honey=User(name='honey',age=22,city='合肥')
gay=User(name='gay',age=32,city='六安')
tong=User(name='tong',age=27,city='霍山')
temp=[tom,jack,bob,honey,gay,tong]
session.add_all(temp)
session.commit()


    

