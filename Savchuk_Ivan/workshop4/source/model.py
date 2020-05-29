from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from OracleDb import *

Base = declarative_base()
db = OracleDb()


class app_user(Base):
    __tablename__ = 'app_user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False)
    user_age = Column(Integer, nullable=False)
    user_phone = Column(String(30), unique=True)
    user_mail = Column(String(30), unique=True)
    user_bank = Column(Integer, unique=True)
    orders_num = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, age, phone, mail, bank, orders_num, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = app_user(user_id=new_id,
                            user_name=name,
                            user_age=age,
                            user_phone=phone,
                            user_mail=mail,
                            user_bank=bank,
                            orders_num=orders_num)
        session.add(new_user)
        session.commit()


class orders(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('app_user.user_id'), nullable=False)
    film_id = Column(Integer, ForeignKey('films.film_id'), nullable=False)
    cinema_id = Column(Integer, ForeignKey('cinema.cinema_id'), nullable=False)
    ticket_id = Column(Integer, ForeignKey('ticket.ticket_id'), nullable=False)
    snack_id = Column(Integer, ForeignKey('snack.snack_id'), nullable=True)
    price = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, film_name, cinema_name, phone, seat, time, new_id=None, price=None, snack=None):
        db = OracleDb()
        session = db.sqlalchemy_session

        ids = session.query(films).filter(films.film_name == film_name)
        id_film = [row.film_id for row in ids][0]
        idd = session.query(cinema).filter(cinema.cinema_name == cinema_name)
        id_cinema = [row.cinema_id for row in idd][0]
        idt = session.query(ticket).filter(and_(ticket.seat == seat,
                                                ticket.ticket_time == time))
        id_ticket = [row.ticket_id for row in idt][0]
        ticket_price = [row.price for row in idt][0]
        idu = session.query(app_user).filter(app_user.user_phone == phone)
        id_user = [row.user_id for row in idu][0]
        snack_price = 0
        id_snack = None
        if snack is not None:
            id_s = session.query(snack).filter(snack.snack_name == snack)
            id_snack = [row.snack_id for row in id_s][0]
            snack_price = [row.price for row in id_s][0]
        new_order = orders(order_id=new_id,
                           user_id=id_user,
                           film_id=id_film,
                           cinema_id=id_cinema,
                           ticket_id=id_ticket,
                           snack_id=id_snack,
                           price=(ticket_price + snack_price)
                           )

        session.add(new_order)
        session.commit()


class cinema(Base):
    __tablename__ = 'cinema'
    cinema_id = Column(Integer, primary_key=True)
    cinema_name = Column(String(30), nullable=False)
    cinema_location = Column(String(30), unique=True)
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


class ticket(Base):
    __tablename__ = 'ticket'
    ticket_id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey('films.film_id'), nullable=False)
    cinema_id = Column(Integer, ForeignKey('cinema.cinema_id'), nullable=False)
    seat = Column(String(30))
    ticket_time = Column(DateTime, nullable=False)
    price = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, film_name, cinema_name, seat, time, price, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session

        ids = session.query(films).filter(films.film_name == film_name)
        id_film = [row.film_id for row in ids][0]
        idd = session.query(cinema).filter(cinema.cinema_name == cinema_name)
        id_cinema = [row.cinema_id for row in idd][0]
        new_ticket = ticket(ticket_id=new_id,
                            film_id=id_film,
                            cinema_id=id_cinema,
                            seat=seat,
                            ticket_time=time,
                            price=price)

        session.add(new_ticket)
        session.commit()


class films(Base):
    __tablename__ = 'films'
    film_id = Column(Integer, primary_key=True)
    film_name = Column(String(30), nullable=False)
    release_date = Column(Date, nullable=False)
    film_description = Column(String(30), nullable=True)
    film_rate = Column(Integer, nullable=True)
    age_constraint = Column(Integer, nullable=False)
    orders_num = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, date, age_constraint, orders_num, new_id=None, description=None, rate=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_film = films(film_id=new_id,
                         film_name=name,
                         release_date=date,
                         film_description=description,
                         film_rate=rate,
                         age_constraint=age_constraint,
                         orders_num=orders_num)
        session.add(new_film)
        session.commit()


class snack(Base):
    __tablename__ = 'snack'
    snack_id = Column(Integer, primary_key=True)
    snack_name = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)
    orders_num = Column(Integer, nullable=False)

    @classmethod
    def add_member(self, name, price, orders_num, new_id=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_snack = snack(snack_id=new_id,
                          snack_name=name,
                          price=price,
                          orders_num=orders_num)
        session.add(new_snack)
        session.commit()


class comments(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    film = Column(String(30), nullable=False)
    comment_text = Column(String(30), nullable=False)
    film_rate = Column(Integer, nullable=True)

    @classmethod
    def add_member(self, film, text, new_id=None, rate=None):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_comment = comments(comment_id=new_id,
                               film=film,
                               comment_text=text,
                               film_rate=rate)
        session.add(new_comment)
        session.commit()


Base.metadata.create_all(db.sqlalchemy_engine)