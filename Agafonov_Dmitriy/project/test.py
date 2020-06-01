import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import user_database, user_question
from collections import Counter


def quantity(values):
    c = Counter(values)
    keys_arr = []
    values_arr = []
    keys = c.keys()
    values = c.values()
    for i in keys:
        keys_arr.append(i)
    for i in values:
        values_arr.append(i)

    return keys_arr, values_arr

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
engine = create_engine(oracle_connection_string.format(

        username="PROJECTDB",
        password="oracle123",
        sid="XE",
        host="localhost",
        port="1521",
        database="PROJECTDB",
    ), echo=True)
Session = sessionmaker(bind=engine)
session = Session()
age_of_user = session.query(user_database.user_age).all()
age_of_user_arr = []
for i in age_of_user:
    age_of_user_arr.append(i[0])
print(age_of_user_arr)

test = quantity(age_of_user_arr)
print(test)
