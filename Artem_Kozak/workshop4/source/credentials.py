import cx_Oracle

username = 'WORKSHOPS'
password = 'WORKSHOPS'
ip = 'localhost'
port = 32118
service_name = 'XE'
dsn = cx_Oracle.makedsn(ip, port, service_name=service_name)
databaseName = dsn

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'WORKSHOPS'
PASSWORD = 'WORKSHOPS'

HOST = 'localhost'
PORT = 32118
SERVICE = 'XE'

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
