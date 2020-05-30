from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, MetaData, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from source.db_connection import engine, connection
from sqlalchemy.sql import or_,and_, between, all_, any_,select
import cx_Oracle
import re
date_is_busy = False
cursor = connection.cursor()
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
    def search_service(namee):
        query2 = 'select SERVICE_NAME from services'
        prserv = cursor.execute(query2)
        all_names = []
        for i in prserv:
            all_names.append(i[0])
        if namee not in (all_names):
            return False
        else:
            service_namee = cursor.callfunc('find_service_name', str, [namee])
            print(service_namee)
            service_price = cursor.callfunc('get_service_price', float, [service_namee])
            return [[service_namee, service_price]]





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
    cars = relationship('Car', back_populates='driver')#one to many relationship4

    @classmethod
    def add(cls, email, first_name, second_name, user_login, user_password, birthday, telephone):
        if not first_name.isalpha() or not second_name.isalpha() or not \
                (x.isalpha() or isinstance(x,int) for x in user_password) or not re.match(r"[^@]+@[^@]+\.[^@]+", email) \
                or not re.match(r'[0]\d{9}$', telephone):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        ids = []
        for i in session.query(Driver):
            ids.append(i.driver_id)
        global a
        a = max(ids)+1
        driver = Driver(driver_id = a, email=email, first_name= first_name, second_name=second_name,user_login=user_login,user_password=user_password,birthday=birthday, telephone=telephone)
        session.add(driver)
        session.commit()

    def authorisation(login, passs):
        a = cursor.callfunc('user_auth.is_user', int, [login, passs])
        if a == 0:
            return 0
        else:
            global current_id
            current_id = cursor.callfunc('user_auth.get_driver_id', int, [login, passs])
            return current_id

    def get_username(idd):
        return cursor.callfunc('user_auth.get_driver_username', str, [idd])

class Car(Base):
    __tablename__ = 'car'
    driver_id = Column(Integer, ForeignKey('driver.driver_id'), primary_key=True)
    car_license_plate = Column(String(30), primary_key=True)
    car_name = Column(String(100), nullable=False)
    car_type = Column(String(40), nullable=False)
    car_color = Column(String(20))
    driver = relationship('Driver', back_populates='cars')
    @classmethod
    def add(cls, car_license_plate, car_name, car_type, car_color):
        #driver_id in session.query(Driver.driver_id).all()
        if not((x.isalpha or isinstance(x,int) for x in car_license_plate) or len(car_license_plate)<10) or not\
                (x.isalpha or x.isspace for x in car_name) or not (car_type=='sedan' or car_type=='crossover' or car_type=='truck')\
                or not (car_color.isalpha):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        car = Car(driver_id=a, car_license_plate=car_license_plate, car_name=car_name,
                                               car_type=car_type, car_color=car_color)
        session.add(car)
        session.commit()


class Wish(Base):
    __tablename__ = 'wish'
    service_name = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    when_date = Column(Date, primary_key=True, nullable=False)
    type_of_car = Column(String(100), nullable=False)
    driver_id = Column(Integer, ForeignKey('driver.driver_id'), nullable=False)
    id1 = relationship('Driver', foreign_keys=[driver_id])
    @classmethod
    def add(cls, service_name, price, when_date, type_of_car,driver_id):
        if not all(x.isalpha() or x.isspace() for x in service_name) or not (
                isinstance(price, float) or isinstance(price, int) or price>0) or not (type_of_car.isalpha or type_of_car=='sedan'\
                or type_of_car=='crossover' or type_of_car=='truck') or not isinstance(driver_id,int):
            print('Data is incorrect!')
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        wish = Wish(service_name=service_name, price=price, when_date = when_date, type_of_car= type_of_car, driver_id = driver_id)
        session.add(wish)
        session.commit()
    def get_price(namee):
        times = cursor.callfunc('give_sale', int, [current_id])
        if (times ==0) or ((times % 5) !=0):
            return int(cursor.callfunc('get_service_price', float, [namee]))
        else:
            return int(cursor.callfunc('get_service_price', float, [namee]))/2
    def free_date(datee):
        dib = cursor.callfunc('date_is_taken_by_someone', int, [datee])
        global date_is_busy
        if dib>0:
            date_is_busy = True
            return date_is_busy
        else:
            return date_is_busy
    def difference_between_dates(datee):
        dates_diff = cursor.callfunc('difference_between_dates', str, [datee])
        print(dates_diff)
        if dates_diff[0] == '+' and int(dates_diff[12]) >= 1:
            print(True)
            return True
        else:
            print(False)
            return False




Base.metadata.create_all(engine)
#Services.add('Discs washing ', 200)
#Driver.add('pasha123@gmail.com', 'Pasha', 'Boyko', 'pasha123', 'pashapasha123', '6-AUG-99', '0668912266')
#Car.add('AC2233AI', 'Toyota Camry', 'sedan', 'black')
#Wish.add('Undercarriage wash', 150, '1-AUG-19', 'crossover', 1)
#Driver.add('artemb@gmail.com', 'Artem', 'Boyko', 'artemb5454', 'artemartem54', '29-OCT-99', '0634567732')

