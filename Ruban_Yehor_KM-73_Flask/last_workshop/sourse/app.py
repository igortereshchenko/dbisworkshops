from flask import Flask, render_template, request
from db_connection import engine
from entities import Customers, Restaurants, Menu, Orders, History, Base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/registration', methods=['POST','GET'])
def create_account():
    if request.method=='POST':
            phone = request.form['phone']
            surname = request.form['surname']
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            row = Customers(name = name, surname = surname, phone = phone, email=email, password = password)
            session.add(row)
            session.commit()
            return render_template('home.html')
    else:
            return render_template('registration.html')


@app.route('/authorization')
def author():
    return render_template('authorization.html')

if __name__ == '__main__':
    app.run(debug=True)

