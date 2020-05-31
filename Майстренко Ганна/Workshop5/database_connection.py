from sqlalchemy.engine import create_engine

# для создания таблиц Вам неободимо прописать путь к своей базе данніх oracle
DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'system'
PASSWORD = 'msn1973msn'

HOST = 'localhost'
PORT = 1521
SERVICE = 'xe'

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
engine = create_engine(ENGINE_PATH_WIN_AUTH)
