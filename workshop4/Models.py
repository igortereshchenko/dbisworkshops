from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Hikes(Base):
    __tablename__ = 'hikes'

    hike_id = Column(Integer, primary_key=True)
    hike_name = Column(String(150))
    duration = Column(Integer)
    complexity = Column(Integer)
    length = Column(Float)
    price = Column(Integer)
    sentences = relationship("Sentences", back_populates="hikes")


class Sentences(Base):
    __tablename__ = 'sentences'

    sentence_id = Column(Integer, primary_key=True)
    fk_hike_id = Column(Integer, ForeignKey('hikes.hike_id'))
    start_date = Column(Date)

    orders = relationship("Orders", back_populates="sentences")
    hikes = relationship("Hikes", back_populates="sentences")


class Orders(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    fk_user_id = Column(Integer, ForeignKey('users.user_id'))
    fk_sentence_id = Column(Integer, ForeignKey('sentences.sentence_id'))

    users = relationship("Users", back_populates="orders")
    sentences = relationship("Sentences", back_populates="orders")


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    fio = Column(String(100))
    birth_date = Column(Date)
    equipment = Column(Integer)
    healthy = Column(Integer)
    height = Column(Float)
    weight = Column(Float)

    orders = relationship("Orders", back_populates="users")


class MasterSQL(object):

    @classmethod
    def Select(cls, orm_table):
        select = session.query(orm_table).all()
        result = [list(row.__dict__.items()) for row in select]
        return result

    @classmethod
    def Insert(cls, insert_row):
        session.add(insert_row)
        session.commit()



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# print(MasterSQL.Select(Hikes)[0][1:])