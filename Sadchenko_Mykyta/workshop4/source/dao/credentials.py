import cx_Oracle

username = 'studentpma'
password = 'qwerty'
ip = 'localhost'
port = 1521
service_name = 'XE'
dsn = cx_Oracle.makedsn(ip, port, service_name=service_name)
databaseName = dsn

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'studentpma'
PASSWORD = 'qwerty'

HOST = 'localhost'
PORT = 1521
SERVICE = 'orcl'

ENGINE_PATH_WITH_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE