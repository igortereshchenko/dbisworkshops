from sql_connection import engine
from ORM_relations import U_USER, SERIES, GRADE, Base
from sqlalchemy.sql import select, update, join
from sqlalchemy import and_, or_, between, asc, desc, update
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def check_user_exist(username):

    try:
        if bool(session.query(Users_users.id).filter_by(id = '1').first()) is False:

            row = U_USER(id = '1',user_username = username)
            session.add(row)
            session.commit()
            search_query = (session.query(U_USER).filter_by(id = '1').one()).user_username

            print('Hello,', search_query)

        else:
            if bool(session.query(U_USER.user_username).filter_by(user_username = username).first()) is True:
                print('User already exist')

            else:
                id_value = session.query(U_USER.id).count()
                row = U_USER(id=id_value+1, user_username=username)
                session.add(row)
                session.commit()

    except:
        print('This user already exsist')


def grade(id,grade,values,id_user,series_id,text):
    if grade > 10:
        print('Max value is 10')
    else:
        row = grade(id=id, grade_value=values,user_id = id_user,series_id = series_id,reviw = text)
        session.add(row)
        session.commit()
