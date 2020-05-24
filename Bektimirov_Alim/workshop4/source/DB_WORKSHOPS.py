from source.credentials import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class OracleDb(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:
                connection = cx_Oracle.connect('WORKSHOPS/WORKSHOPS@XE')
                cursor = connection.cursor()
                oracle_connection_string = 'oracle+cx_oracle://WORKSHOPS:WORKSHOPS@DESKTOP-MTUVCRU:1521/?service_name=XE'
                engine = create_engine(oracle_connection_string)
                Session = sessionmaker(bind=engine)
                session = Session()

                OracleDb._instance.sqlalchemy_session = session
                OracleDb._instance.sqlalchemy_engine = engine
                OracleDb._instance.connection = connection
                OracleDb._instance.cursor = cursor

            except Exception as error:
                print('Error: connection not established {}'.format(error))

        return cls._instance

    def __init__(self):
        oracle_connection_string = 'oracle+cx_oracle://WORKSHOPS:WORKSHOPS@DESKTOP-MTUVCRU:1521/?service_name=XE'
        engine = create_engine(oracle_connection_string)
        Session = sessionmaker(bind=engine)
        session = Session()
        self.sqlalchemy_session = session
        self.sqlalchemy_engine = engine
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor


    def execute(self, query):
        try:
            result = self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print('error executing query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.sqlalchemy_session.close()


if __name__ == "__main__":
    db = OracleDb()
