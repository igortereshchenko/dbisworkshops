from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from source.DB_WORKSHOPS import *

Base = declarative_base()
db = OracleDb()

# liked_users = Table('liked_users',
#     Column('film_id', Integer, ForeignKey('liked_film_list.film_id')),
#     Column('user_id', Integer, ForeignKey('bot_user.user_id'))
# )



class Bot_user(Base):
    __tablename__ = 'bot_user'
    user_id = Column(Integer,primary_key=True)
    user_name = Column(String(30), nullable=False)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=True)
    liked_films = relationship('Liked_film_list', secondary='liked_users')
    expec_films = relationship('Expected_film_list', secondary='expected_users')
    @classmethod
    def add(self, user_id, user_name, first_name, last_name):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = Bot_user(
            user_id=user_id,
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
        )
        session.add(new_user)
        session.commit()

class Liked_film_list(Base):
    __tablename__ = 'liked_film_list'
    film_id = Column(Integer, primary_key=True)
    film_name = Column(String(30), nullable=False)
    genre = Column(Integer, nullable=False)
    release_date = Column(Integer, nullable=False)
    rating = Column(Float(precision=1), nullable=False)
    user = relationship('Bot_user', secondary='liked_users')
    @classmethod
    def add(self, film_id, film_name, genre, release_date, rating):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_film = Liked_film_list(
            film_id=film_id,
            film_name=film_name,
            genre=genre,
            release_date=release_date,
            rating=rating,
        )
        session.add(new_film)
        session.commit()

class Expected_film_list(Base):
    __tablename__ = 'expected_film_list'
    film_id = Column(Integer, primary_key=True)
    film_name = Column(String(30))
    genre = Column(Integer, nullable=False)
    release_date = Column(Integer, nullable=False)
    rating = Column(Float(precision=1), nullable=False)
    user = relationship('Bot_user', secondary='expected_users')
    @classmethod
    def add(self, film_id, film_name, genre, release_date, rating):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_film = Expected_film_list(
            film_id=film_id,
            film_name=film_name,
            genre=genre,
            release_date=release_date,
            rating=rating,
        )
        session.add(new_film)
        session.commit()


class Liked_users(Base):
    __tablename__ = 'liked_users'
    film_id = Column(Integer,ForeignKey('liked_film_list.film_id'), primary_key=True)
    user_id = Column(Integer,ForeignKey('bot_user.user_id'), primary_key=True)

class Expec_users(Base):
    __tablename__ = 'expected_users'
    film_id = Column(Integer,ForeignKey('expected_film_list.film_id'), primary_key=True)
    user_id = Column(Integer,ForeignKey('bot_user.user_id'), primary_key=True)



# liked_users = Table('liked_users',
#     Column('film_id', Integer, ForeignKey('liked_film_list.film_id')),
#     Column('user_id', Integer, ForeignKey('bot_user.user_id'))
# )

Base.metadata.create_all(db.sqlalchemy_engine)