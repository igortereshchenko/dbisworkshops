
from flask import Flask, render_template, url_for, redirect, request, session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Expenditure import Expenditure, Card
from flask_sqlalchemy import SQLAlchemy

from forms import ExpenditureForm, CreateCard, Monitor
import plotly
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import json


def pie(values1, values2, values3, values4, values5):
    labels = ['travel', 'medecine', 'food', 'clothes', 'entertaiment']
    values = [values1, values2, values3, values4, values5]

    # Use hole to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, marker_colors=['rgb(39, 32, 29)', 'rgb(41, 55, 29)', 'rgb(78, 55, 29)',
                                                'rgb(78, 55, 78)', 'rgb(78, 81, 78)'])])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pasha'
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
app.config['SQLALCHEMY_DATABASE_URI'] = oracle_connection_string.format(

            username="SYSTEM",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT",
        )
db = SQLAlchemy(app)


@app.route("/", methods=['GET'])
def hello():
    return render_template('hello.html')


@app.route('/index', methods=["GET", "POST"])
def vitrati():
    form = ExpenditureForm()
    if form.is_submitted():
         try:
        oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

        engine = create_engine(oracle_connection_string.format(

            username="SYSTEM",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT",
        ), echo=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        result = request.form
        adddata = Expenditure(result['time'], result['cost_value'], result['category_name'], result['card_number'])
        session.add(adddata)
        session.commit()
        return render_template('confirmIsOkey.html', result=result)

     except:
    	result = request.form
    	return render_template('confirmIsNotOkey.html', result = result)

    return render_template('index.html', form=form)


@app.route('/card', methods=["GET", "POST"])
def tocreatecard():
    form = CreateCard()
    if form.is_submitted():
         try:
        oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
        engine = create_engine(oracle_connection_string.format(

            username="SYSTEM",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT"),
            echo=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        result = request.form
        adddata = Card(result['card_number'], result['money_amount'])
        session.add(adddata)
        session.commit()
        return render_template('confirmIsOkey.html', result=result)

     except:
    	result = request.form
    	return render_template('confirmIsNotOkey.html', result = result)

    return render_template('card.html', form=form)




@app.route('/monitor',  methods=['GET', 'POST'])
def monitor():
    global current_page
    #result=db.session.query(tour).filter_by(tour_name="Paris dream").first()
    #print('result:', result)
    current_page = "monitor"
    form = Monitor()
    if form.is_submitted():
        oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

        engine = create_engine(oracle_connection_string.format(

            username="SYSTEM",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT",
        ), echo=True)

        Session = sessionmaker(bind=engine)
        session_orm = Session()
        select = db.session.query(Expenditure).filter_by(time=form.time.data, category_name= form.category_name.data ).all()
        print(select)
        results=[]
        for row in select:
            results.append(row.cost_value)

        if 'search_results' in session:
            session.pop('search_results', None)

            session['search_results'] = results
        else:
            session['search_results'] = results

        return redirect(url_for('result'))

    return render_template("monitor.html", form = form)



@app.route('/result/')
def result():
    global current_page
    current_page = "result"
    if 'search_results' in session:
        results = session.get('search_results')
    else:
        results = []
    return render_template("result.html", results=results)


@app.route('/analyse',  methods=['GET', 'POST'])
def graphs():
    travel=len(db.session.query(Expenditure).filter_by(category_name="travel").all())
    medecine = len(db.session.query(Expenditure).filter_by(category_name="medecine").all())
    food = len(db.session.query(Expenditure).filter_by(category_name="food").all())
    clothes = len(db.session.query(Expenditure).filter_by(category_name="clothes").all())
    entertaiment = len(db.session.query(Expenditure).filter_by(category_name="entertaiment").all())
    print(travel, medecine, food, clothes, entertaiment)

    checker1 = 0

    if travel == 0 and medecine == 0 and food == 0 and clothes == 0 and entertaiment == 0:
        checker1 = 1

    pie_graph1 = pie(travel, medecine, food, clothes, entertaiment)
    return render_template('analyse.html', plot1=pie_graph1,  checker1=checker1)



if __name__ == "__main__":
    app.run(debug=True)