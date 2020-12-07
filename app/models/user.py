from .. import db
import datetime,logging
from sqlalchemy import UniqueConstraint
from werkzeug.security import generate_password_hash, check_password_hash
from ..common.exceptions import DBError
from flask_login import UserMixin
from app import login

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10),nullable=False)
    hashed_password = db.Column(db.Float,nullable=False)
    active = db.Column(db.Boolean(),default=False)
    user_id = db.Column(db.String(100),nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    __table_args__ = (
        UniqueConstraint('username'),
    )

    @login.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    @staticmethod
    def save_user(username,password):
        try:
            u = User(username=username,hashed_password=generate_password_hash(password))
            db.session.add(u)
            db.session.commit()
            db.session.close()
        except Exception as e:
            raise DBError(e)

    @staticmethod
    def verify_password(username,password):
        try:
            pswd = db.session.query(User.hashed_password).filter(User.username == username).first()
            if check_password_hash(pswd,password):
                logging.info("Password match")
                return True
            return False
        except Exception as e:
            raise DBError(e)


    @staticmethod
    def get_user_name(username):
        try:
            uid = db.session.query(User.user_id).filter(User.username == username).first()
            logging.info("Returning user id %s " % uid)
            return uid
        except Exception as e:
            logging.info("Exception on getting user id by username %s " % username)
            raise DBError(e)
