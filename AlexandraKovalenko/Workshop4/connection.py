'''
import os

username = 'postgres'
password = '1111'
host = '127.0.0.1'
port = '5432'
database = 'meddb'
DATABASE_URI = os.getenv("DATABASE_URL",'postgres+psycopg2://postgres:{}@{}:{}/{}'.format(password, host, port, database))
'''
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:1111@127.0.0.1:5432/meddb')