from flask import Blueprint,render_template

analysis=Blueprint('analysis',__name__,url_prefix='/analysis')

@analysis.route("/")
def index():
    return render_template('analysis.html')
