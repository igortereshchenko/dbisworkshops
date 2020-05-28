DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'DUMMY'
PASSWORD = 'DUMB'

HOST = 'localhost'
PORT = 32118
SERVICE = 'XE'

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
