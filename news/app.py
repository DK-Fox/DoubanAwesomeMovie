from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
import json
import os
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/news'
db=SQLAlchemy(app)

JSON_DIR='/home/shiyanlou/files/'

class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    def __init__(self,name):
        self.name=name

    def __expr__(self):
        return '<Category %r>'%self.name

class File(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    created_time=db.Column(db.DateTime)
    category_id=db.Column(db.Integer,db.ForeignKey('category.id'))
    category=db.relationship('Category',backref=db.backref('files',lazy='dynamic'))
    content=db.Column(db.Text)
    def __init__(self,title,created_time,category,content):
        self.title=title
        self.created_time=created_time
        self.category=category
        self.content=content

    def __expr__(self):
        return '<Title %r>'%self.title


class Json():
    def __init__(self,filename):
        with open(filename) as f:
            self._data=json.load(f)

    @property
    def data(self):
        return self._data

@app.route('/')
def index():
    files=File.query.all()
    return render_template('index.html',files=files)

@app.route('/files/<file_id>')
def file(file_id):
    f=File.query.filter_by(id=int(file_id)).all()
    if len(f)==1:
        ef=f[0]
        c=Category.query.filter_by(id=ef.category_id).all()
        if len(c)==1:
            ec=c[0]
            return render_template('file.html',cur_file=ef,cur_category=ec)
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__=='__main__':
    app.run(port=3000)
