from database_connection import engine
from db_classes import Categories, Dishes, Clients, Marks,Base
from sqlalchemy.sql import select, update, join
from sqlalchemy import and_, or_, between, asc, desc,update
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def check_user_exist(username):

    try:
        

        if bool(session.query(Clients.id).filter_by(id = '1').first()) is False:

            row = Clients(id = '1',client_username = username)
            session.add(row)
            session.commit()
            search_query = (session.query(Clients).filter_by(id = '1').one()).client_username

            print('Hello,', search_query)

        else:
            if bool(session.query(Clients.client_username).filter_by(client_username = username).first()) is True:
            
                print('User already exist') 

            else:
                id_value = session.query(Clients.id).count()
                row = Clients(id=id_value+1, client_username=username)
                session.add(row)
                session.commit()

    except:
        print('This user already exsist')



def check_mark_value(id,mark,values,id_client,dish_id,text):
    if mark > 5:
        print('Max value is 5')
    else:
        row = Marks(id=id, mark_value=values,client_id = id_client,dish_id = dish_id,text_reviw = text)
        session.add(row)
        session.commit()

def check_is_dish_exist(dish_name):
    if bool(session.query(Dishes.dish_name).filter_by(dish_name = dish_name).first()) is False:
        print('This dish is not exist in our database')
    else:
        result = session.query(Dishes).filter(Dishes.dish_name == dish_name).one()).text_recipe
        print("Recipe:", result)



