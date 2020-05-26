from sqlalchemy import create_engine
from dao.credentials import *

oracle_connection = 'oracle+cx_oracle://{}:{}@{}'.format(username, pasword, databaseName)
engine = create_engine(oracle_connection)
