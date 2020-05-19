from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, MetaData, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from source.db_connection import engine
from sqlalchemy.sql import or_,and_, between, all_, any_,select
import re

Base = declarative_base()
meta = MetaData()

class Services(Base):
    __tablename__ = 'services'
    service_name = Column(String(100), primary_key=True, nullable=False)
    price = Column(Float(8, 2), primary_key=True, nullable=False)
    CheckConstraint('price > 0', name='check_price')
    @classmethod
    def add(cls, service_name, price):
        if not all(x.isalpha()or x.isspace() for x in service_name) or not (isinstance(price, float) or isinstance(price, int)) :
            print('Data is incorrect!')
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        services = Services(service_name = service_name, price=price)
        session.add(services)
        session.commit()





class Driver(Base):
    __tablename__ = 'driver'
    driver_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(50),  nullable=False, unique=True)
    first_name = Column(String(100), nullable=False)
    second_name = Column(String(100))
    user_login = Column(String(40), nullable=False, unique=True)
    user_password = Column(String(50), nullable=False)
    birthday = Column(Date)
    telephone = Column(String(30), nullable=False, unique=True)
    cars = relationship('Car', back_populates='driver')#one to many relationship
    @classmethod
    def add(cls, driver_id, email, first_name, second_name, user_login, user_password, birthday, telephone):
        if not isinstance(driver_id, int) or not first_name.isalpha() or not second_name.isalpha() or not \
                (x.isalpha() or isinstance(x,int) for x in user_password) or not re.match(r"[^@]+@[^@]+\.[^@]+", email) \
                or not re.match(r'[0]\d{9}$', telephone):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        driver = Driver(driver_id = driver_id, email=email, first_name= first_name, second_name=second_name,user_login=user_login,user_password=user_password,birthday=birthday, telephone=telephone)
        session.add(driver)
        session.commit()

class Car(Base):
    __tablename__ = 'car'
    driver_id = Column(Integer, ForeignKey('driver.driver_id'), primary_key=True)
    car_license_plate = Column(String(30), primary_key=True)
    car_name = Column(String(100), nullable=False)
    car_type = Column(String(40), nullable=False)
    car_color = Column(String(20))
    driver = relationship('Driver', back_populates='cars')
    @classmethod
    def add(cls, driver_id, car_license_plate, car_name, car_type, car_color):
        #driver_id in session.query(Driver.driver_id).all()
        if not (isinstance(driver_id, int)) or not\
            ((x.isalpha or isinstance(x,int) for x in car_license_plate) or len(car_license_plate)<10) or not\
                (x.isalpha or x.isspace for x in car_name) or not (car_type=='sedan' or car_type=='crossover' or car_type=='truck')\
                or not (car_color.isalpha):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        car = Car(driver_id=driver_id, car_license_plate=car_license_plate, car_name=car_name,
                                               car_type=car_type, car_color=car_color)
        session.add(car)
        session.commit()


class Wish(Base):
    __tablename__ = 'wish'
    service_name = Column(String(100), ForeignKey('services.service_name'),primary_key=True, nullable=False)
    price = Column(Integer, ForeignKey('services.price'), primary_key=True, nullable=False)
    when_date = Column(Date, nullable=False, unique=True)
    type_of_car = Column(String(100), nullable=False)
    services = relationship("Services", foreign_keys=[service_name])
    services1 = relationship("Services", foreign_keys=[price])
    @classmethod
    def add(cls, service_name, price, when_date, type_of_car):
        if not all(x.isalpha() or x.isspace() for x in service_name) or not (
                isinstance(price, float) or isinstance(price, int) or price>0) or not (type_of_car.isalpha or type_of_car=='sedan'\
                or type_of_car=='crossover' or type_of_car=='truck'):
            print('Data is incorrect!')
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        wish = Wish(service_name=service_name, price=price, when_date = when_date, type_of_car= type_of_car)
        session.add(wish)
        session.commit()



Base.metadata.create_all(engine)
#Services.add('Undercarriage wash', 150)
#Driver.add(2, 'pasha123@gmail.com', 'Pasha', 'Boyko', 'pasha123', 'pashapasha123', '6-AUG-99', '0668912266')
#Car.add(1, 'AC2233AI', 'Lamborghini Huracan', 'sedan', 'yellow')
#Wish.add('Undercarriage wash', 150, '1-AUG-19', 'crossover')

