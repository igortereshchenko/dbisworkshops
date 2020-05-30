from sqlalchemy.engine import create_engine
import cx_Oracle

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'MYONLINEEDU'
PASSWORD = 'MYONLINEEDU'

HOST = 'localhost'
PORT = 1521
SERVICE = 'xe'

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

engine = create_engine(ENGINE_PATH_WIN_AUTH)

databaseName = "localhost:1521/xe"
connection = cx_Oracle.connect(USERNAME, PASSWORD, databaseName)