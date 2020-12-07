from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_httpauth import HTTPBasicAuth


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login = LoginManager()
login.session_protection = 'strong'


def create_app(config_name):
    app = Flask(__name__)
    auth = HTTPBasicAuth()
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login.init_app(app)

    # register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .homebase import dashboard as dash
    app.register_blueprint(dash,url_prefix='/dashboard')

    from .api import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api')

    return app
