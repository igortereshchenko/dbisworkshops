from sqlalchemy import Column, String, DateTime, Integer, MetaData, ForeignKey, CheckConstraint
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_conn import engine
from cheker import book_check, re, user_check


meta = MetaData()
Base = declarative_base()


class Book(Base):
    __tablename__ = 'book'
    book_id = Column(Integer, primary_key=True, nullable=False)
    book_name = Column(String(50), primary_key=False, nullable=False)
    author_name = Column(String(50), primary_key=False, nullable=False)
    author_lastname = Column(String(50), primary_key=False, nullable=False)
    book_url = Column(String(70), primary_key=False, nullable=False)
    CheckConstraint('book_id > 0', name='check_id')

    @classmethod
    def add_book(cls, b_id, b_name, a_name, a_lname, b_url):
        b_check = book_check(b_id, a_name, a_lname)
        if not b_check:
            print("data is incorrect")
            return -1
        else:
            Session = sessionmaker(bind=engine)
            session = Session()
            new_book = Book(book_id = b_id, book_name=b_name, author_name=a_name, author_lastname=a_lname,
                            book_url=b_url)
            session.add(new_book)
            session.commit()


class User(Base):
    __tablename__='l_user'
    user_name = Column(String(50), primary_key=False, nullable=True)
    user_lastname = Column(String(50), primary_key=False, nullable=True)
    email = Column(EmailType, primary_key=True, nullable=False)
    registration = Column(DateTime, primary_key=False,nullable=False)
    login = Column(String(20), primary_key=False, nullable=False)
    password = Column(String(30), primary_key=False, nullable=False)
    book_amount = Column(Integer, primary_key=False, nullable=True)
    CheckConstraint('book_amount>=0', name='ba_ch')

    @classmethod
    def add_user(cls, name, last_name,email,  registration, login, psw, amount):
        u_check = user_check(name, last_name, email, registration, amount)
        if not u_check:
            print("data is incorrect")
            return -1
        else:
            Session = sessionmaker(bind=engine)
            session = Session()
            new_user = User(user_name=name, user_lastname=last_name, email=email, registration=registration,
                            login=login,password=psw,book_amount=amount)
            session.add(new_user)
            session.commit()


class UserBook(Base):
    __tablename__ = 'user_book'
    t_book_id = Column(Integer, ForeignKey('book.book_id'), primary_key=True, nullable=False)
    user_email = Column(EmailType, ForeignKey('l_user.email'), primary_key=True, nullable=False)
    CheckConstraint('t_book_id>0', name='t_book_check')

    @classmethod
    def add_user_book(cls, b_id, u_email):
        if not isinstance(b_id, int) or not re.match(r"[^@]+@[^@]+\.[^@]+", u_email):
            print('Data is incorrect')
            return -1
        else:
            Session = sessionmaker(bind=engine)
            session = Session()
            new_user_book = UserBook(t_book_id=b_id, user_email=u_email)
            session.add(new_user_book)
            session.commit()
