from flask import Flask, flash, redirect, url_for, session, g
from flask import request
from flask import render_template

from collections import Counter

import plotly
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import json

import cx_Oracle

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import user_database, user_question
import sqlalchemy

from forms import SignUpForm, LogInForm, CreateQuestion

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jinja'


def pie(keys, values):
    #labels  = values
    fig = go.Figure(data=[go.Pie(labels=keys, values=values)])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def quantity(values):
    c = Counter(values)
    keys_arr = []
    values_arr = []
    keys = c.keys()
    values = c.values()
    for i in keys:
        keys_arr.append(i)
    for i in values:
        values_arr.append(i)

    return keys_arr, values_arr

@app.route("/")
@app.route("/home")
def home():
    #if g.sess_var:
       # return render_template('home.html', result = session['sess_var'])
    return render_template('home.html')


@app.before_request
def before_request():
    g.sess_var = None

    if 'sess_var' in session:
        sess_var = session['sess_var']
        g.sess_var = sess_var



@app.route('/registration', methods=["GET", "POST"])
def registration():
    form = SignUpForm()
    if form.validate_on_submit():
        try:


            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

            engine = create_engine(oracle_connection_string.format(

                username="PROJECTDB",
                password="oracle123",
                sid="XE",
                host="localhost",
                port="1521",
                database="PROJECTDB",
            ), echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            add_data = user_database(result['user_name'], result['user_mail'], result['user_age'], result['edrpou'], result['user_pass'])
            session.add(add_data)
            session.commit()
            return render_template("home.html")

           # session['sess_user_name'] = request.form['']

        except:
            #result = request.form
            return render_template('register.html')

    return render_template('register.html', form=form)



@app.route('/login', methods=["GET", "POST"])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        try:
            conn = cx_Oracle.connect('PROJECTDB/oracle123@localhost/XE')
            cur = conn.cursor()
            cur.execute('select * from USER_TABLE')
            data = []
            for i in cur:
                data.append(i)
            cur.close()
            conn.close()
            mail = form.user_mail.data
            passw = form.user_pass.data

            c1 = 0
            for i in data:
                c1 += 1
                for j in i:
                    if j == passw and mail == data[c1 - 1][2]:
                        #print('ok')
                        # username = data[c1 - 1][1]


                        user = data[c1 - 1][0]
                        print(user)
                        session.pop('sess_var', None)
                        session['sess_var'] = user
                        return render_template('home.html', result=session['sess_var'])


                        #return render_template('question.html')

        except:
            #session['sess_var'] = 'error'
            return render_template('notOk.html')

    return render_template('login.html', title='Login', form=form)





@app.route('/question', methods=["GET", "POST"])
def question():
    form = CreateQuestion()

    if form.validate_on_submit():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
            engine = create_engine(oracle_connection_string.format(

                username="PROJECTDB",
                password="oracle123",
                sid="XE",
                host="localhost",
                port="1521",
                database="PROJECTDB",
            ), echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            add_data = user_question(result['user_id'], result['question_reference'], result['question'], result['time_creating'], 1)
            session.add(add_data)
            session.commit()
            return render_template('Ok.html', result=result)

        except:
           #result = request.form
            return render_template('notOk.html')

    return render_template('question.html', form=form)


@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
    engine = create_engine(oracle_connection_string.format(

        username="PROJECTDB",
        password="oracle123",
        sid="XE",
        host="localhost",
        port="1521",
        database="PROJECTDB",
    ), echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    age_of_user = session.query(user_database.user_age).all()
    age_of_user_arr = []
    for i in age_of_user:
        age_of_user_arr.append(i[0])
    print(age_of_user_arr)

    test = quantity(age_of_user_arr)
    print(test)

    pie_graph = pie(test[0], test[1])
    #return render_template('graphs.html', plot1=pie_graph)


    return render_template('dashboard.html', plot1=pie_graph)

"""""
@app.route('/dropsession')
def drop_session():
    session.pop('sess_var', None)
    return render_template('login.html')
"""""

if __name__ == "__main__":
    app.run(debug=True)