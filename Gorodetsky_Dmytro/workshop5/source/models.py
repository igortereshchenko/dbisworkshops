from sqlalchemy import Integer, String, Column, Float, ForeignKey, CheckConstraint, \
    create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import cx_Oracle
from database_connection import USERNAME, PASSWORD, PATH
import re
connection = cx_Oracle.connect(USERNAME, PASSWORD, PATH)
cursor = connection.cursor()

engine = create_engine("oracle+cx_oracle://"+USERNAME+":"+PASSWORD+"@"+PATH)
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, ForeignKey('carts.book_id'), primary_key=True)
    book_name = Column(String(200), nullable=False)
    author = Column(String(80),  nullable=False)
    price = Column(Float, nullable=False)
    genre = Column(String(50), nullable=False)
    on_storage = Column(Integer, nullable=False)
    book_description = Column(String(500), nullable=False)
    book_edition = Column(String(50), nullable=False)
    number_of_purchases = Column(Integer, nullable=False)
    CheckConstraint('price > 0', name='check_price')
    CheckConstraint('on_storage >= 0', name='check_number_of_purchases')
    CheckConstraint('number_of_purchases >=0', name='check_on_storage')

    @classmethod
    def get_author_by_username(cls, bookname):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Book).filter(Book.book_name == bookname).one()
        return result.author

    @classmethod
    def get_price_by_username(cls, bookname):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Book).filter(Book.book_name == bookname).one()
        return result.price

    @classmethod
    def get_id_by_username(cls, bookname):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Book).filter(Book.book_name == bookname).one()
        return result.book_id

    @classmethod
    def get_genre_by_username(cls, bookname):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Book).filter(Book.book_name == bookname).one()
        return result.genre

    @classmethod
    def get_edition_by_username(cls, bookname):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Book).filter(Book.book_name == bookname).one()
        return result.book_edition


class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, ForeignKey('carts.customer_id'), primary_key=True)
    first_name = Column(String(100), nullable=False)
    second_name = Column(String(100))
    email = Column(String(40), nullable=False)
    user_login = Column(String(40), nullable=False)
    user_password = Column(String(50), nullable=False)

    @classmethod
    def register_user(cls, first_name, second_name, email, login, pass1, pass2):
        for var in [first_name, second_name, login, email, pass1, pass2]:
            if var == '':
                var = None

        if pass1 == pass2:
            msg = cursor.var(cx_Oracle.STRING)
            cnt = cursor.var(cx_Oracle.NUMBER)
            cursor.callproc("registration_p.register_user",
                            [first_name, second_name, login, email, pass1, pass2, cnt, msg])
            connection.commit()
            return msg.getvalue()
        else:
            return "Введені паролі не співпадають"

    @classmethod
    def perform_authorisation(cls, user_login, password):
        for var in [user_login, password]:
            if var == '':
                var = None
        customer_id = cursor.callfunc("authorisation_p.authorisation", cx_Oracle.NUMBER, [user_login, password])
        return int(customer_id)

    @classmethod
    def get_username(cls, customer_id):

        if customer_id == '':
            customer_id = None

        if customer_id == -1:
            return "Такого користувача не існує"
        user_login = cursor.callfunc("authorisation_p.get_username", cx_Oracle.STRING, [customer_id])
        return user_login

    @classmethod
    def get_user_by_username(cls, username):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Customer).filter(Customer.user_login == username).one()
        return result

    @classmethod
    def get_id_by_username(cls, username):
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.query(Customer).filter(Customer.user_login == username).one()
        return result.customer_id


class Cart(Base):
    __tablename__ = 'carts'
    customer_id = Column(Integer, ForeignKey('customers.customer_id'), primary_key=True)
    book_id = Column(Integer, ForeignKey('books.book_id'), primary_key=True)
    book_name = Column(String(200), nullable=False)
    author = Column(String(80), nullable=False)
    price = Column(Float, nullable=False)
    genre = Column(String(50), nullable=False)
    book_edition = Column(String(50), nullable=False)

# Session = sessionmaker(bind=engine)
#
# session = Session()
# book = Book(book_id=4, book_name="4", author="4", price=4, genre="4", on_storage = 4, book_description = "4",
#             book_edition = "4", number_of_purchases = 4)
#
# session.add(book)
#
# session.commit()
Base.metadata.create_all(engine)
