from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db= SQLAlchemy()

class Base(db.Model):
    __abstract__=True

    create_time=db.Column(db.DateTime,default=datetime.utcnow)
    update_time=db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

class DoubanMovie(Base):
    __tablename__ = 'DoubanMovie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    url =db.Column(db.String(128))
    year=db.Column(db.Integer)
    type=db.Column(db.String(64))
    location=db.Column(db.String(64))
    summary=db.Column(db.Text)
    score=db.Column(db.Float)

class User(Base, UserMixin):
    __tablename__='user'

    #普通用户和管理员
    ROLE_USER=10
    ROLE_ADMIN=20

    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(32),unique=True,index=True,nullable=False)
    email=db.Column(db.String(64),unique=True,index=True,nullable=False)
    _password=db.Column('password',db.String(256),nullable=False)
    role=db.Column(db.SmallInteger,default=ROLE_USER)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,original_passwd):
        self._password=generate_password_hash(original_passwd)

    def check_password(self,password):
        return check_password_hash(self._password,password)

    @property
    def is_admin(self):
        return self.role==self.ROLE_ADMIN
