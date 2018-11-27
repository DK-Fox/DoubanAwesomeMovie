from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

engine=create_engine('mysql+mysqldb://root:123456@mymysql:3306/lagouinf?charset=utf8')
Base=declarative_base()

class Lagouinf(Base):
    __tablename__ = 'information'

    id = Column(Integer, primary_key=True)
    # name = Column(String(64))
    # update_time = Column(DateTime)

if __name__=='__main__':
    Base.metadata.create_all(engine)
