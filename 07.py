#!/home/xiezhengdong/.local/bin/python
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,Integer,Float,Date
from sqlalchemy.ext.declarative import declarative_base
engine=create_engine('mysql+pymysql://gua:123456@localhost:3306/dong')
Base=declarative_base(bind=engine)
Session=sessionmaker(bind=engine)
class User(Base):
    __tablename__='usr'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20),unique=True)
    age=Column(Integer)
Base.metadata.create_all()
tom=User(name='tom',age='20')
bob=User(name='bob',age='19')
jack=User(name='jack',age='20')
session=Session()
num=[tom,bob,jack]
session.add_all(num)
session.commit()
