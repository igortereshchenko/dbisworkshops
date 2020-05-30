from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
import cx_Oracle
from sqlalchemy import create_engine
from forms import *

app = Flask(__name__)

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{database}'
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

db = SQLAlchemy()

class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seats_number = db.Column(db.Integer, default=1)
    location_description = db.Column(db.String(100), default='New table')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column('email', db.String(50), nullable=False)
    name = db.Column('name', db.String(100), nullable=False)
    password = db.Column('password', db.String(50), nullable=False)

user_orders = db.Table('user_order',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column('description', db.String(200), default='No special description')
    month = db.Column('order_month', db.String(20), nullable=False)
    day = db.Column('order_day', db.Integer, nullable=False)
    time = db.Column('order_time_begin', db.Integer, nullable=False)
    table = db.Column(db.Integer, db.ForeignKey('tables.id'))
    tables = db.relationship("Table")

@app.route('/')
def index():
    return render_template("user.html", form=UserForm()) 

if __name__=='__main__':
    app.run()
