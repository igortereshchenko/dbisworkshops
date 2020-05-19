from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    
    SECRET_KEY = environ.get('ZviahinKey')
    FLASK_ENV = environ.get('ZviahinEnv')
    FLASK_APP = 'main.py'
    FLASK_DEBUG = 1

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
