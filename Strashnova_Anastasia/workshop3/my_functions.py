from connection_to_db import engine
from db import Users, Code, Books, User_books, Base, User_list
from sqlalchemy.sql import select, update, join
from sqlalchemy import and_, or_, between, asc, desc,update
from sqlalchemy.orm import sessionmaker
import time


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()



                                        #Реєстрація користувача


def create_account(code_1, email_1, password_1):
    try:

        if (session.query(Code).filter_by(code_id=code_1).first()).action != 1:

            update = session.query(Code).filter_by(code_id=code_1).first()
            update.action = 1
            session.merge(update)

            row = Users(email=email_1 , code_id = code_1, password = password_1)
            session.add(row)
            search_query = (session.query(Code).filter_by(code_id = code_1).one()).name

            print('hello,', search_query)

        else:
            print('this account is already exist')
    except :
        print('ups something wrong')


#create_account('NM56777755','john', 'password44')


                                        #Вхід в аккаунт

def log_in(email,password):
        try:
                check=session.query(Users).filter_by(email=email,password=password).all()
                for i in check:
                        id=i.code_id

                get_name = session.query(Code).filter_by(code_id=id).all()
                for i in get_name:
                        print('Welcome,', i.name)

        except:
                print('damn')

#log_in('email','password')


                                        #Пошук за критеріями


def search_by_criteria(title, author, year):
        try:
            if title!= None and author!=None and year!= None:
                 search_query = session.query(Books).filter_by(author = author, title = title, year=year).all()
            elif title!= None and author!=None:
                search_query = session.query(Books).filter_by(author=author, title=title).all()
            elif author!=None and year!= None:
                search_query = session.query(Books).filter_by(author=author, year=year).all()
            elif title!= None and year!= None:
                search_query = session.query(Books).filter_by(title=title, year=year).all()
            elif title != None:
                search_query = session.query(Books).filter_by(title=title).all()
            elif author != None:
                search_query = session.query(Books).filter_by(author=author).all()
            elif year != None:
                search_query = session.query(Books).filter_by(year=year).all()

            for row in search_query:
                print(row.title, row.author, row.year)

        except:
            print("try again")




#search_by_criteria(None, None, None)

                                #Перегляд списока обраного
def show_favourites(user_id):
        list = session.query(User_list).filter_by(user_id=user_id, b_in_basket=None).all()
        for row in list:
                search_query = session.query(Books).filter_by(id=row.wish_list).all()
                for i in search_query:
                        print(i.title, i.author, i.year)


                                        #Перегляд кошика
def show_basket(user_id):
        list = session.query(User_list).filter_by(user_id=user_id, wish_list=None).all()
        for row in list:
                search_query = session.query(Books).filter_by(id=row.b_in_basket).all()
                for i in search_query:
                        print(i.title, i.author, i.year)



#show_favourites('NM11111111')
#show_basket('NO90909090')

                                #Користувач додає книгу в список обраного
def put_in_favourites(user_id, id):
        if (session.query(User_list).filter_by(wish_list=id, user_id = user_id).first())==None:
                row = User_list(user_id=user_id, wish_list=id)
                session.add(row)
                show_favourites(user_id)
        else:
                show_favourites(user_id)


#put_in_favourites('NM11111111', 1111)


                                #Зміна кількості книжок в бд

def count_of_books(action, id):
        count_1 = session.query(Books).filter_by(id=id).all()
        if (action == 'in') :
                for i in count_1 :
                        cote = (i.count) - 1

        if (action == 'out'):
                for i in count_1:
                        cote = (i.count) + 1

        update = session.query(Books).filter_by(id=id).first()
        update.count = cote
        session.merge(update)



                                     #Автоматичне видалення з кошика

def delete_after_24_hours( user_id,id ):
        time.sleep(5)# i will change to 24 hours
        if (session.query(User_list).filter_by(user_id=user_id, b_in_basket=id).first()) != None:
                delete_query = session.query(User_list).filter_by(b_in_basket=id, user_id=user_id).one()
                session.delete(delete_query)
                count_of_books('out', id)
        else:
                print('nema')
                None




                                        #Додати в кошик

def put_in_basket(user_id, id):
        if (session.query(User_list).filter_by(user_id = user_id, b_in_basket=id).first())==None:
                row = User_list(user_id=user_id, b_in_basket=id)
                session.add(row)
                count_of_books('in', id)
                show_basket(user_id)
                #delete_after_24_hours(user_id, id)
        else:
                print('already there')
                show_basket(user_id)


#put_in_basket('NM11111111', 1111)

#delete_after_24_hours('NO90909090', 1234)

                                        #Видалити зі списку обраного

def delete_from_favourites(user_id, id):
        delete_query = session.query(User_list).filter_by(wish_list=id, user_id=user_id).one()
        session.delete(delete_query)
        show_favourites(user_id)



#delete_from_favourites('NM11111111', 1111)


                                         # Оформити замовлення

def place_the_order(from_where ,user_id, id):
        list=[]
        a=session.query(User_books).filter_by(user_id = user_id).all()
        for i in a:
                list.append(i.books)
        if len(list)<7:
                list_2 = []
                a_2 = session.query(User_books).filter_by(user_id=user_id, books=id).all()
                for i in a_2:
                        list_2.append(i.books)
                if len(list_2)<3:
                        row = User_books(user_id=user_id, books=id, placement= 'library')
                        session.add(row)
                        if from_where == 'basket':
                                delete_query = session.query(User_list).filter_by(b_in_basket=id, user_id=user_id).one()
                                session.delete(delete_query)
                        else:
                                count_of_books('in', id)

                        print('Ми отримали Ваше замовлення. Обробка займе не більше 10 хвилин. Після чого можете отримати Вашу літературу')

                else:
                        print('You can not have more than 3 identical books')

        else:
                print('You can not have more than 7 librarian books')


#place_the_order('basket' ,'NM11111111', 1111)


                                  #Користувач отримав книгу
def recieve_book(user_id, id):
        update = session.query(User_books).filter_by(user_id =user_id,books=id, placement='library').first()
        update.placement = 'home'
        session.merge(update)

#recieve_book('NM11111111', 1111)

                                #Користувач повернув книжку

def back_to_library(user_id, id):
        delete_query = session.query(User_books).filter_by(user_id=user_id, books=id, placement='home').one()
        session.delete(delete_query)
        count_of_books('out', id)


#back_to_library('NM11111111', 1111)

session.commit()

