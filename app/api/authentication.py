__author__ = 'chenfeiyu'
from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from . import api
from .errors import unauthorized
from ..common import utils
from ..models.user import User

auth = HTTPBasicAuth()


# This is a callback method of HTTPBasicAuth
@auth.verify_password
def verify_password(username, password):
    if utils.is_empty(username) or utils.is_empty(password):
        return False

    if User.verify_password(username,password):
        g.current_user = User.get_user_name(username)
        return True
    else:
        return False


@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials')


# This will affect the whole blue print
# @api.before_request
# @auth.login_required
# def before_request():
#     if g.current_user != Config.USER_NAME:
#         return forbidden('Unconfirmed account')
