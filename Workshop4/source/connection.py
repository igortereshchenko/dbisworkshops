from sqlalchemy.engine import create_engine

username = 'user'
password = '1234'
sid = 'XE'
host = 'localhost'
port = '1521'


oracle_connection_path = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
engine = create_engine(oracle_connection_path)