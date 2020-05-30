import cx_Oracle
username = 'TEST'
password = '240580'
ip = 'localhost'
port = 1521
service_name = 'cochalka'
dsn = cx_Oracle.makedsn(ip, port, service_name=service_name)
databaseName = dsn

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'TEST'
PASSWORD = '240580'

HOST = 'localhost'
PORT = 1521
SERVICE = 'cochalka'

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE