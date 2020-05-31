from database_connection import engine
from db_classes import Categories, Dishes, Clients, Marks,Base
from sqlalchemy.sql import select, update, join
from sqlalchemy import and_, or_, between, asc, desc,update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import plotly.express as px
import plotly.graph_objects as go



# Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# функция для добавления нового пользователя
def check_user_exist(username):

    try:
        # q = session.query(Clients).filter_by(Clients.id == '1')

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
                row = Clients(id = id_value+1, client_username = username)
                session.add(row)
                session.commit()
                print('We successfully added you to our database')

    except:
        print('This user already exsist')

# функция для проверки значения оценки
def check_mark_value(id,mark,values,id_client,dish_id,text):
    if mark > 5:
        print('Max value is 5')
    else:
        row = Marks(id=id, mark_value=values,client_id = id_client,dish_id = dish_id,text_reviw = text)
        session.add(row)
        session.commit()
# bool(User.query.filter_by(name='John Smith').first())

# функция для проверки существования блюда
def check_is_dish_exist(dish_name):
    # exsist = session.query(Dishes).filter(Dishes.dish_name == dish_name)
    if bool(session.query(Dishes.dish_name).filter_by(dish_name = dish_name).first()) is False:
        return False

    else:
        return True
#
def if_not_exist_dish():

    result = session.query(Dishes.dish_name).all()
    return 'Такого блюда не существует в нашей базе данных, посмотрите блюда, которые доступны',result

def result_of_search(dish_name):

    result = (session.query(Dishes).filter(Dishes.dish_name == dish_name).one())
    return result.ingridients, result.text_recipe

 # функция для получения видео рецепта
def get_video_recipe(dish_name):
    # exsist = session.query(Dishes).filter(Dishes.dish_name == dish_name)
    if bool(session.query(Dishes.dish_name).filter_by(dish_name = dish_name).first()) is False:
        return False
    else:
        return True

def get_exsist_video_recipe(dish_name):
    result = (session.query(Dishes).filter(Dishes.dish_name == dish_name).one()).video_recept
    return result
# функция для добавления оценки пользователя
def add_user_mark(mark,client_username,dish_name):

    if bool(session.query(Marks.id).filter_by(id='1').first()) is False:
        id_found = (session.query(Clients).filter(Clients.client_username == client_username).first()).id
        dish_id = (session.query(Dishes).filter(Dishes.dish_name == dish_name).first()).id


        row = Marks(id= '1', mark_value = mark, client_id = id_found, dish_id = dish_id,user_name = client_username)
        session.add(row)
        session.commit()
        return 'Вы наш первый пользователь.Мы успешно добавили вашу первую оценку'

    elif bool(session.query(Marks).filter(Marks.user_name == client_username).first()) is True:
        session.query(Marks).filter(Marks.user_name == client_username).update({Marks.mark_value: mark},synchronize_session=False)
        session.commit()
        return 'Мы успешно обновили вашу оценку'
    else:
        id_found = (session.query(Clients).filter(Clients.client_username == client_username).one()).id
        dish_id = (session.query(Dishes).filter(Dishes.dish_name == dish_name).one()).id
        id_value = session.query(Marks.id).count()
        row = Marks(id=id_value + 1, mark_value = mark, client_id = id_found, dish_id = dish_id, user_name = client_username)
        session.add(row)
        session.commit()
        return 'Мы успешно добавили вашу оценку'
# функция для проверки принадлежности блюда к категории
def check_dish_category(dish_name):
    id_dish = (session.query(Dishes).filter(Dishes.dish_name == dish_name).one()).id
    dish_category = (session.query(Categories).filter(Categories.id == id_dish).one()).category_name
    return dish_category
# функция добавления комментария пользователя в бд
def add_comments(message,username):

    session.query(Marks).filter(Marks.user_name == username).update({Marks.text_reviw: message},synchronize_session = False)
    session.commit()
    return 'Мы успешно добавили ваш комментарий'
# функции для просмотре блюд и коментариев
def see_users_comments():
    return session.query(Marks.user_name,Marks.text_reviw).all()

def see_all_soups():
    return (session.query(Dishes.dish_name).filter(Dishes.id_category == 1).all())

def see_all_main_dishes():
    return (session.query(Dishes.dish_name).filter(Dishes.id_category == 3).all())

def see_all_salads():
    return (session.query(Dishes.dish_name).filter(Dishes.id_category == 2).all())

def see_all_desserts():
    return (session.query(Dishes.dish_name).filter(Dishes.id_category == 4).all())

# график распределения оценок пользователей
def statistic_of_marks():
    result = []
    for i in range(1,6):
        result.append(session.query(Marks).filter(Marks.mark_value== i).count())

    return result
def avarage_of_mark():

    result = session.query(func.avg(Marks.mark_value).label('average')).all()
    #
    # sum_of_marks = session.query(Marks.mark_value).all()
    return round((result[0][0]),1)
    # num_of_marks = len(sum_of_marks)
    # result = sum(sum_of_marks)/num_of_marks
    # print(result)


















