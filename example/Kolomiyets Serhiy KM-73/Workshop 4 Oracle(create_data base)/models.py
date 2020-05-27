from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from OracleDB import OracleDb
import datetime

Base = declarative_base()
db = OracleDb()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    @classmethod
    def add_category(self, name, description):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_category = Category(
            name=name,
            description=description,
        )
        session.add(new_category)
        session.commit()
        self.id = new_category.get_id(name)

    @classmethod
    def get_id(self, name):
        db = OracleDb()
        q = db.execute(f"select id from categories where name='{name}'")  # f-formatstring
        return q[0][0]

    @classmethod
    def get_all(self):
        db = OracleDb()
        q = db.execute("select * from categories")
        return q


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(Integer)
    price = Column(Integer)
    description = Column(String)
    color = Column(String)
    amount = Column(Integer)
    available = Column(String)
    country = Column(String)
    material = Column(String)
    cat = Column(Integer)
    model = Column(String)

    @classmethod
    def add_product(self, name, code, price, description, color, amount, country, material, cat, model):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_product = Product(
            name=name,
            code=code,
            price=price,
            description=description,
            color=color,
            amount=amount,
            available="y" if amount > 0 else "n",
            country=country,
            material=material,
            cat=cat,
            model=model
        )
        session.add(new_product)
        session.commit()
        self.id = new_product.get_id(code)

    @classmethod
    def get_id(self, code):
        db = OracleDb()
        q = db.execute(f"select id from products where code='{code}'")  # f-formatstring
        return q[0][0]

    @classmethod
    def get_all(self):
        db = OracleDb()
        q = db.execute("select * from products")
        return q


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    code = Column(Integer)
    phone = Column(String)
    email = Column(String)
    amount = Column(Integer)
    city = Column(String)
    street = Column(String)
    order_date = Column(Date)

    @classmethod
    def add_order(self, surname, code, phone, email, amount, city, street):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_order = Order(
            surname=surname,
            code=code,
            phone=phone,
            email=email,
            amount=amount,
            city=city,
            street=street,
            order_date=datetime.datetime.utcnow()
        )
        session.add(new_order)
        session.commit()
        self.id = new_order.get_id(phone)

    @classmethod
    def get_id(self, phone):
        db = OracleDb()
        q = db.execute(f"select id from orders where phone='{phone}'")  # f-formatstring
        return q[0][0]

    @classmethod
    def get_all(self):
        db = OracleDb()
        q = db.execute("select * from orders")
        return q
