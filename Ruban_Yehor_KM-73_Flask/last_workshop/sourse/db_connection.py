import pymysql
from sqlalchemy.engine import create_engine
pymysql.install_as_MySQLdb()

engine = create_engine("mysql://root:ronalda17@localhost/alchemy")