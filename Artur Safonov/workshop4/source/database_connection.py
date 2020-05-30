from sqlalchemy.engine import create_engine


DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'

USERNAME = 'SYSTEM'
PASSWORD = 'oracle'

HOSTNAME = 'localhost'
PORT = 1521
SERVICE = 'xe'

ENGINE_PATH_WITH_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOSTNAME + ':' + str(PORT) + '/?service_name=' + SERVICE

engine = create_engine(ENGINE_PATH_WITH_AUTH)
