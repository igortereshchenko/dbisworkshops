from sqlalchemy import create_engine

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(
    oracle_connection_string.format(
        username='DBPROJECT',
        password='111',
        hostname='localhost',
        port='1521',
        database='orcl',
    )
)