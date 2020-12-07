import os

basedir = os.path.abspath(os.path.dirname(__file__))

__author__ = 'tomas'
class Config:
    USER_NAME = os.environ.get('USER_NAME') or 'homebase'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'admin'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_RECYCLE = 45

    MAIL_SERVER = '*********'
    MAIL_PORT = 00
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[Homebase Alert]'
    MAIL_SENDER = '******@******'
    MAIL_USE_SSL = False

    SQLALCHEMY_POOL_SIZE = 0

    DATABASE_URL_LOCAL = 'mysql+pymysql://flask_app:keeshan@localhost/homebase'

    #mqtt config
    MQTT_CLIENT_ID = ''

    @staticmethod
    def init_app(app):
        pass


# mysql+pymysql://username:password@url/database
class DevelopmentConfig(Config):
    #DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or Config.DATABASE_URL_LOCAL

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or Config.DATABASE_URL_LOCAL

# json ?
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}