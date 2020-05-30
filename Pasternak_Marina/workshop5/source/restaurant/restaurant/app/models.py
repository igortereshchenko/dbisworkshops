from . import db

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
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
    def __repr__(self):
        return f"{{'name': '{self.name}', 'email': '{self.email}', 'password':'{self.password}'}}"

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

    def __init__(self, month, day, time, table, description=None):
        self.month = month
        self.day = day
        self.time = time
        self.table = table
        self.description = description
    
    def __repr__(self):
        return f"""{{'month': '{self.month}', 'day': '{self.day}', 'time':'{self.time}', "
                "'table': '{self.table}', 'description':'{self.description}'}}"""
    