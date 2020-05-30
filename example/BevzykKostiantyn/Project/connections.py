from sqlalchemy import create_engine
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/?service_name={database}'

engine = create_engine(
    oracle_connection_string.format(
        username="MYDATABASE",
        password="qwert123",
        hostname="localhost",
        port='1521',
        database='XE'
    )
)