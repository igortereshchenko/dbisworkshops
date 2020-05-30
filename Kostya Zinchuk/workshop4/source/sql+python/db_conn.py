from sqlalchemy.engine import create_engine

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'MYDATABASE'
PASSWORD = 'oracle123'
PATH = "localhost:1521/xe"

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + PATH
engine = create_engine(ENGINE_PATH_WIN_AUTH)
