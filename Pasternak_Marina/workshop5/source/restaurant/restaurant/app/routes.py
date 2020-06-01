import os
import json
import ast
from flask import current_app as app
from flask import (jsonify, 
                    abort, 
                    render_template, 
                    redirect, 
                    request)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import db, User, Order

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/order/", methods=['GET', 'POST'])
def order_values():
    return render_template('order.html')

@app.route("/login/", methods=['GET', 'POST'])
def login_values():
    return render_template('login.html')

@app.route("/schedule/", methods=['GET', 'POST'])
def watch_schedule():
    return render_template('schedule.html')

@app.route('/test_profile', methods=['GET', 'POST'])
def return_users():
    dictionaty_db = User.query.all()
    value_begin = ','.join([str(value) for value in dictionaty_db])
    test = value_begin
    test = test.replace("\'", "\"")
    return test

@app.route('/insert_login', methods=['GET', 'POST'])
def add_data():
    if request.method == "POST":
        request_form = request.form
        email = request_form['mail']
        name = request_form['name']
        password = request_form['password']
        value = User(email, name, password)
        db.session.add(value)
        db.session.commit()
    return render_template('index.html')

@app.route('/test_order', methods=['GET', 'POST'])
def return_orders():
    dictionaty_db = Order.query.all()
    value_begin = ','.join([str(value) for value in dictionaty_db])
    test = value_begin
    test = test.replace("\'", "\"")
    return test

@app.route('/insert_order', methods=['GET', 'POST'])
def add_order():
    if request.method == "POST":
        request_form = request.form
        month = request_form['month']
        day = request_form['order_date']
        time = request_form['order_time_begin']
        table = request_form['table']
        description = request_form['description']
        value = Order(month, day, time, table, description)
        db.session.add(value)
        db.session.commit()
    return render_template('index.html')