from sqlalchemy import Integer, String, Column, MetaData, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType
from database_connection import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import re
Base = declarative_base()
meta = MetaData()


class nutrition(Base):
    __tablename__ = 'nutrition'
    nutr_title = Column(String(100), primary_key=True, nullable=False)
    nutr_brand = Column(String(40), primary_key=True, nullable=False)
    nutr_price = Column(Float, primary_key=True, nullable=False)
    nutr_weight = Column(Float, primary_key=True, nullable=False)
    nutr_ingredient = Column(String(30), primary_key=True, nullable=False)
    nutr_description = Column(String(500), nullable=False)
    CheckConstraint('price > 0', name='check_price')
    CheckConstraint('weight > 0', name='check_weight')



    @classmethod
    def add(cls, nutr_title, nutr_brand, nutr_price, nutr_weight, nutr_ingredient, nutr_description):
        if not nutr_title.isalpha() or not nutr_brand.isalpha() or not nutr_ingredient.isalpha() or not nutr_description.isalpha() \
                or not isinstance(nutr_price, float) or not isinstance(nutr_weight, float):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        Nutrition = nutrition(nutr_title=nutr_title, nutr_brand=nutr_brand, nutr_price=nutr_price, nutr_weight=nutr_weight, nutr_ingredient=nutr_ingredient,
                    nutr_description=nutr_description)
        session.add(Nutrition)
        session.commit()

class customer(Base):
    __tablename__ = 'customer'

    cust_name = Column(String(80), nullable=False)
    cust_surname = Column(String(90))
    cust_login = Column(String(40), primary_key=True, nullable=False)
    cust_password = Column(String(50), nullable=False)
    cust_email = Column(EmailType, nullable=False)
    cust_adress = Column(String(300), nullable=False)

    @classmethod
    def add(cls, cust_name, cust_surname, cust_login, cust_password, cust_email, cust_adress):
        if not cust_name.isalpha() or not cust_surname.isalpha() or not cust_login.isalpha() or not cust_password.isalpha()  \
                or not cust_adress.isalpha() or not re.match(r"[^@]+@[^@]+\.[^@]+", cust_email):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        Customer1 = customer(cust_name=cust_name, cust_surname=cust_surname, cust_login=cust_login, cust_password=cust_password,
                    cust_email=cust_email, cust_adress=cust_adress)
        session.add(Customer1)
        session.commit()


class review(Base):
    __tablename__ = 'review'
    nutr_title = Column(String(100), ForeignKey('nutrition.nutr_title'), primary_key=True, nullable=False)
    nutr_brand = Column(String(40), ForeignKey('nutrition.nutr_brand'), primary_key=True, nullable=False)
    nutr_price_fk = Column(Float, ForeignKey('nutrition.nutr_price'))
    nutr_ingredient_fk = Column(String(30), ForeignKey('nutrition.nutr_ingredient'))
    reviews = Column(String(600), nullable=False)
    rating = Column(Integer, nullable=False)
    CheckConstraint('nutr_price_fk >= 0', name='check_nutr_price_fk')
    CheckConstraint('rating >= 0', name='check_rating')
    nutritions = relationship("nutrition", foreign_keys=[nutr_title])
    nutritions_brand = relationship("nutrition", foreign_keys=[nutr_brand])
    nutritions_price = relationship("nutrition", foreign_keys=[nutr_price_fk])
    nutritions_ingredient = relationship("nutrition", foreign_keys=[nutr_ingredient_fk])

    @classmethod
    def add(cls, nutr_title, nutr_brand, nutr_price_fk, nutr_ingredient_fk, reviews, rating):
        if  not nutr_title.isalpha() or not nutr_brand.isalpha() \
                or not isinstance(nutr_price_fk, float) or not nutr_ingredient_fk.isalpha() or not reviews.isalpha() \
                 or not isinstance(rating, int):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        review1 = review(nutr_title=nutr_title, nutr_brand=nutr_brand, nutr_price_fk=nutr_price_fk,
                         nutr_ingredient_fk=nutr_ingredient_fk, reviews=reviews, rating=rating)
        session.add(review1)
        session.commit()


class cust_order(Base):
    __tablename__ = 'cust_order'

    nutr_title = Column(String(100), ForeignKey('nutrition.nutr_title'), primary_key=True, nullable=False)
    nutr_brand = Column(String(40), ForeignKey('nutrition.nutr_brand'), primary_key=True, nullable=False)
    nutr_price = Column(Float, ForeignKey('nutrition.nutr_price'))
    nutr_ingredient_fk = Column(String(30), ForeignKey('nutrition.genre'), nullable=False)
    status = Column(String(25), nullable=False)
    CheckConstraint('price >= 0', name='check_price')
    nutritions = relationship("nutrition", foreign_keys=[nutr_title])
    nutritions_brand = relationship("nutrition", foreign_keys=[nutr_brand])
    nutritions_price = relationship("nutrition", foreign_keys=[nutr_price])
    nutritions_ingredient = relationship("nutrition", foreign_keys=[nutr_ingredient_fk])

    @classmethod
    def add(cls, nutr_title, nutr_brand, nutr_price, nutr_ingredient_fk, status):
        if not nutr_title.isalpha() or not nutr_brand.isalpha() \
                or not isinstance(nutr_price, float) or not nutr_brand.isalpha() or not status.isalpha():
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        cust_order1 = cust_order(nutr_title=nutr_title, nutr_brand=nutr_brand, nutr_price=nutr_price, nutr_ingredient_fk=nutr_ingredient_fk,
                                 status=status)
        session.add(cust_order1)
        session.commit()


Base.metadata.create_all(engine)