import os
from flask_restful import Api
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))
script_dir = os.path.dirname(__file__)

CSRF_ENABLED = True
SECRET_KEY = 'Replace_With_SecretKey'

api = Api(app)

