from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Flask Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_APP = 'restaurant.py'
    FLASK_DEBUG = 1

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../restaurant.db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False