from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from OracleDb import *

Base = declarative_base()
db = OracleDb()

#          Створення таблиць сутностей


class app_user(Base):
    __tablename__ = 'app_user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    user_age = Column(Integer, nullable=False)
    user_phone = Column(String(30), unique=True)
    user_mail = Column(String(30))
    user_bank = Column(Integer, unique=True)
    city = Column(String(30))
    status = Column(String(30), nullable=False)

    @classmethod
    def add_member(self, name, age, phone, mail, bank, city, status, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = app_user(user_id=new_id,
                            user_name=name,
                            user_age=age,
                            user_phone=phone,
                            user_mail=mail,
                            user_bank=bank,
                            city=city,
                            status=status)
        session.add(new_user)
        session.commit()


class orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('app_user.user_id'), nullable=False)
    movie = Column(String(30), nullable=False)
    cinema_id = Column(String(30), nullable=False)
    seat = Column(String(30), nullable=False)
    snack = Column(String(30), nullable=True)
    datte = Column(String(30), nullable=False)
    time = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, film, cinema, city, phone, seat, date, time, price, new_id=None, snack=None):
        db = OracleDb()
        session = db.sqlalchemy_session

        idu = session.query(app_user).filter(app_user.user_phone == phone)
        id_user = [row.user_id for row in idu][0]

        idc = db.execute(f"SELECT cinema_id FROM cinema WHERE cinema_name = '{cinema}' AND cinema_location = '{city}'")
        id_cine = [row[0] for row in idc][0]

        new_order = orders(order_id=new_id,
                           user_id=id_user,
                           movie=film,
                           cinema_id=id_cine,
                           seat=seat,
                           snack=snack,
                           price=price,
                           datte=date,
                           time=time
                           )
        print(new_order)
        session.add(new_order)
        session.commit()


class cinema(Base):
    __tablename__ = 'cinema'
    cinema_id = Column(Integer, primary_key=True)
    cinema_name = Column(String(30), nullable=False)
    cinema_location = Column(String(30), nullable=False)
    orders_num = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, location, orders_num, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_cinema = cinema(cinema_id=new_id,
                            cinema_name=name,
                            cinema_location=location,
                            orders_num=orders_num
                            )
        session.add(new_cinema)
        session.commit()


class films(Base):
    __tablename__ = 'films'
    film_id = Column(Integer, primary_key=True)
    film_name = Column(String(30), nullable=False)
    age_limit = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, age_limit, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_film = films(film_id=new_id,
                         film_name=name,
                         age_limit=age_limit
                         )
        session.add(new_film)
        session.commit()


class snack(Base):
    __tablename__ = 'snack'
    snack_id = Column(Integer, primary_key=True)
    snack_name = Column(String(30), nullable=False)
    age_limit = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    orders_num = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, price, orders_num, age_limit, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_snack = snack(snack_id=new_id,
                          snack_name=name,
                          age_limit=age_limit,
                          price=price,
                          orders_num=orders_num
                          )
        session.add(new_snack)
        session.commit()


class comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    film = Column(String(30), nullable=False)
    comment_text = Column(String(30), nullable=False)

    @classmethod
    def add_member(self, film, text, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_comment = comments(comment_id=new_id,
                               film=film,
                               comment_text=text,
                               )
        session.add(new_comment)
        session.commit()


Base.metadata.create_all(db.sqlalchemy_engine)
