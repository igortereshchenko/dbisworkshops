import cx_Oracle

username = 'PMA_KM_20'
password = 'oracle_2'
ip = 'localhost'
port = 1521
service_name = 'XE'
dsn = cx_Oracle.makedsn(ip, port, service_name=service_name)
databaseName = dsn