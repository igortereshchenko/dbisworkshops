import cx_Oracle
import os

username = "shop_user"
password = "1234"
databaseName = "localhost:1521/shop"
ip = 'localhost'
port = 1521
sid = "shop"
# dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'shop')
# CONN = cx_Oracle.connect('sys', 'abc', dsn_tns, mode=cx_Oracle.SYSDBA)

os.environ['path'] = "C:\oracle_odbc"
print(os.environ['path'])
connection = cx_Oracle.connect(username, password, databaseName, encoding="UTF-8")
cursor = connection.cursor()
cursor.execute("SELECT user FROM dual")
for i in cursor:
    print(i)

