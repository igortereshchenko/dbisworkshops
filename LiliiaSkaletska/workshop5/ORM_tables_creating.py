
from sqlalchemy import create_engine, CheckConstraint,Sequence, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
engine = create_engine(
    oracle_connection_string.format(

        username="PROJECT",
        password="Oracle",
        sid="XE",
        host="localhost",
        port="1521",
        database="PROJECT",

    )
    , echo=True
)

Base = declarative_base()

class customer (Base):
    __tablename__ = 'customer'
    id = Column(Integer, Sequence('id_seq'))
    message = Column(String(100), nullable=False)
    customer_name = Column(String(30), nullable=False)
    age = Column(Integer, CheckConstraint('age >= 16'),nullable=False)
    email = Column(String(30), CheckConstraint('LENGTH(email) >= 7'), primary_key=True)
    tour_name = Column(String(30),  ForeignKey('tour.tour_name'), primary_key= True)


    def __init__(self, message, customer_name, age, email, tour_name):
        """"""
        self.message = message
        self.customer_name = customer_name
        self.age = age
        self.email = email
        self.tour_name = tour_name

class feedback (Base):
   __tablename__ = 'feedback'
   tour_name = Column(String(30), ForeignKey('tour.tour_name'), primary_key=True)
   group_name = Column(String(30), nullable=False, primary_key=True)
   feedback_message = Column(String(200))

   def __init__(self,tour_name, group_name, feedback_message):
        """"""
        self.tour_name = tour_name
        self.group_name = group_name
        self.feedback_message = feedback_message



class tour (Base):
    __tablename__ = 'tour'
    tour_name = Column(String(30), primary_key=True)
    country = Column(String(30), nullable=False)
    year_category = Column(String(30), nullable=False)
    tour_duration =Column(String(30), nullable=False)
    price_range = Column(String(30), nullable=False)
    tour_price = Column(Integer, nullable=False)

    def __init__(self, tour_name, country, year_category, tour_duration):
        """"""
        self.tour_name = tour_name
        self.country = country
        self.year_category = year_category
        self.tour_duration = tour_duration

Base.metadata.create_all(engine)




