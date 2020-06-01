import os
from Sadchenko_Mykyta.workshop4.source.credentials import ENGINE_PATH_WITH_AUTH


class Config:
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
	SQLALCHEMY_DATABASE_URI = ENGINE_PATH_WITH_AUTH
	SQLALCHEMY_TRACK_MODIFICATIONS = False
