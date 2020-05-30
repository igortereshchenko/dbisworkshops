import cx_Oracle
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
                engine = create_engine('oracle+cx_oracle://{0}:{1}@{2}:{3}/{4}'.format(username,password,ip,port,sid))
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
        engine = create_engine('oracle+cx_oracle://{0}:{1}@{2}:{3}/{4}'.format(username,password,ip,port,sid))
        Session = sessionmaker(bind=engine)
        session = Session()
        self.sqlalchemy_session = session
        self.sqlalchemy_engine = engine
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

        
    def execute(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result
    