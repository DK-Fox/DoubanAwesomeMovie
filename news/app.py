from flask import Flask,render_template
import json

app=Flask(__name__)

JSON_DIR='/home/shiyanlou/files/'
JSON_FILE1='helloshiyanlou.json'
JSON_FILE2='helloworld.json'

class Json():
    def __init__(self,filename):
        with open(filename) as f:
            self._data=json.load(f)

    @property
    def data(self):
        return self._data

@app.route('/')
def index():
    jd1=Json(JSON_DIR+JSON_FILE1).data
    jd2=Json(JSON_DIR+JSON_FILE2).data
    #jd=[jd1['title'],jd2['title']]
    #return render_template('index.html',filenames=jd)
    return jd1['title']+jd2['title']

@app.route('/files/<filename>')
def file(filename):
    for jd in [JSON_FILE1,JSON_FILE2]:
        if filename==jd.split('.')[0]:
            return render_template('file.html',content=Json(JSON_DIR+jd).data['content'])
    abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__=='__main__':
    app.run(port=3000)
