from sqlalchemy.engine import create_engine

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'MYONLINEEDU'
PASSWORD = 'MYONLINEEDU'

HOST = 'localhost'
PORT = 1521
SERVICE = 'xe'

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
engine = create_engine(ENGINE_PATH_WIN_AUTH)