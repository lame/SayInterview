import os
from app import app
from flask_cors import CORS
from flask_restful import Api

basedir = os.path.abspath(os.path.dirname(__file__))
script_dir = os.path.dirname(__file__)

CSRF_ENABLED = True
SECRET_KEY = 'Replace_With_SecretKey'

cors = CORS(app)
api = Api(app)
