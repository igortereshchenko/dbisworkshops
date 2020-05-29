import cx_Oracle
import datetime
from credentials import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class OracleDb(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:
                connection = cx_Oracle.connect(username, password, databaseName)
                cursor = connection.cursor()

                # execute a statement
                cursor.execute('SELECT * FROM v$version')

                # display the PostgreSQL database server version
                db_version = cursor.fetchone()
                print("New connection to {} created".format(db_version[0]))
                oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
                engine = create_engine(oracle_connection_string.format(username="PMA_KM_20", password="oracle_2", sid="XE", host="localhost", port="1521", database="PMA_KM_20"))

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
        oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
        engine = create_engine(oracle_connection_string.format(username=username, password=password, sid=service_name, host=ip, port=port, database=databaseName))

        Session = sessionmaker(bind=engine)
        session = Session()

        self.sqlalchemy_session = session
        self.sqlalchemy_engine = engine
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def execute(self, query):
        '''
        Функція, що дозволяє робити
        запити з бд
        '''
        try:
            result = self.cursor.execute(query)
            self.connection.commit()
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.sqlalchemy_session.close()


if __name__ == "__main__":
    # створюємо екземпляр класу ОраклДб
    db = OracleDb()
