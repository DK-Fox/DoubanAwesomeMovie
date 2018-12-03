from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, Float

engine=create_engine('mysql+mysqldb://root:123456@mymysql:3306/douban_movie?charset=utf8')
Base=declarative_base()

class DoubanMovie(Base):
    __tablename__ = 'DoubanMovie'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    url =Column(String(128))
    year=Column(Integer)
    type=Column(String(64))
    location=Column(String(64))
    summary=Column(Text)
    score=Column(Float)

if __name__=='__main__':
    Base.metadata.create_all(engine)
