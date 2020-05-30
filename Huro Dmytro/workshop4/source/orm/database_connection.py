
from sqlalchemy.engine import create_engine


username = 'postgres'
password = 'root'
host = 'localhost'
database_name = 'postgres'

ENGINE_PATH_WIN_AUTH = 'postgresql://%s:%s@%s/%s'%(username,password,host,database_name)

engine = create_engine(ENGINE_PATH_WIN_AUTH)