from flask import Flask, render_template
from flask_migrate import Migrate
from website.config import configs
from website.models import db,DoubanMovie,User
from flask_login import LoginManager

def register_extensions(app):
    db.init_app(app)
    Migrate(app,db)

    login_manager=LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view='index.login'

def register_blueprints(app):
    from .handlers import admin, analysis, index, movie
    app.register_blueprint(admin)
    app.register_blueprint(analysis)
    app.register_blueprint(index)
    app.register_blueprint(movie)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    register_extensions(app)
    register_blueprints(app)

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'),404

    return app

