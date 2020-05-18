import pymysql.cursors
from sqlalchemy.engine import create_engine


engine = create_engine("mysql://root:useruser@localhost/KPIlibrary",isolation_level="READ UNCOMMITTED")


