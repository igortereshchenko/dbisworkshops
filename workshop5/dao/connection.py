from sqlalchemy.engine import create_engine

oracle_connection_string = 'oracle+cx_oracle://system:oracle@localhost:1521/xe'
engine = create_engine(oracle_connection_string, max_identifier_length=128)