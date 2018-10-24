from flask import Flask,render_template,abort
import json
import os

app=Flask(__name__)

JSON_DIR='/home/shiyanlou/files/'

class Json():
    def __init__(self,filename):
        with open(filename) as f:
            self._data=json.load(f)

    @property
    def data(self):
        return self._data

@app.route('/')
def index():
    jd=[]
    print(os.listdir(JSON_DIR))
    for file in os.listdir(JSON_DIR):
        jd.append(Json(JSON_DIR+file).data['title'])
    return render_template('index.html',filenames=jd)

@app.route('/files/<filename>')
def file(filename):
    if filename+'.json' in os.listdir(JSON_DIR):
        return render_template('file.html',content=Json(JSON_DIR+filename+'.json').data['content'])
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__=='__main__':
    app.run(port=3000)
