from sqlalchemy.engine import create_engine


username = 'postgres'
password = 'toor'
host = 'localhost'
database_name = 'test_db'

ENGINE_PATH_WIN_AUTH = 'postgresql://%s:%s@%s/%s'%(username,password,host,database_name)

engine = create_engine(ENGINE_PATH_WIN_AUTH)