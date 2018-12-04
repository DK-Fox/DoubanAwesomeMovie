from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(dict(
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@mymysql/douban_movie',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    DEBUG=True
))

db= SQLAlchemy(app)

class DoubanMovie(db.Model):
    __tablename__ = 'DoubanMovie'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    url =db.Column(db.String(128))
    year=db.Column(db.Integer)
    type=db.Column(db.String(64))
    location=db.Column(db.String(64))
    summary=db.Column(db.Text)
    score=db.Column(db.Float)

    def __init__(self,name,url,year,type,location,summary,score):
        self.name=name
        self.url=url
        self.year=year
        self.type=type
        self.location=location
        self.summary=summary
        self.score=score

@app.route("/")
def index():
    return render_template('index.html',movies=DoubanMovie.query.all())

# @app.route("/<int:id>")
# def movies(id):
    # movie=DoubanMovie.query.get_or_404(id)
    # return render_template('movie.html',movie=movie)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
