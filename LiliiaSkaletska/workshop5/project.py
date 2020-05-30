from flask import Flask, render_template, url_for, redirect, request, session
from forms import ContactForm, Feedback, FindTour
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM_tables_creating import customer, feedback, tour
from flask_sqlalchemy import SQLAlchemy
import plotly
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import json


def pie(values1, values2, values3, values4):
    labels = ['summer', 'autumn', 'spring', 'winter']
    values = [values1, values2, values3, values4]

    # Use hole to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3, marker_colors=['rgb(246, 255, 0)', 'rgb(250, 151, 37)', 'rgb(186, 242, 73)',
                                                'rgb(87, 148, 153)'])])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

global current_page
current_page = "index"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
app.config['SQLALCHEMY_DATABASE_URI'] = oracle_connection_string.format(

            username="PROJECT",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT",
        )
db = SQLAlchemy(app)

@app.route('/',  methods=['GET', 'POST'])
def index():
    global current_page
    current_page = "index"
    form = FindTour()
    if form.is_submitted():
        oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

        engine = create_engine(oracle_connection_string.format(

            username="PROJECT",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT",
        ), echo=True)

        Session = sessionmaker(bind=engine)
        session_orm = Session()
        print(form.country.data)
        select = db.session.query(tour).filter_by(country=form.country.data, year_category= form.year_category.data, tour_duration= form.tour_duration.data, price_range=form.price_range.data).all()
        print(select)
        results=[]
        for row in select:
            results.append(row.tour_name)



        if 'search_results' in session:
            session.pop('search_results', None)

            session['search_results'] = results
        else:
            session['search_results'] = results

        return redirect(url_for('package'))

    return render_template("index.html", form = form)



@app.route('/package/')
def package():
    global current_page
    current_page = "package"
    if 'search_results' in session:
        secresults = session.get('search_results')
    else:
        secresults = []
    return render_template("package.html", results=secresults)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    global current_page
    current_page = "contact"
    form = ContactForm()
    if form.is_submitted():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

            engine = create_engine(oracle_connection_string.format(

                username="PROJECT",
                password="Oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="PROJECT",
            ), echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = customer(result['message'], result['customer_name'], result['age'], result['email'], result['tour_name'])
            session.add(adddata)
            session.commit()
            return render_template('contactsubmit.html', result=result)

        except:
           result = request.form
           return render_template('submitfail.html', result=result)
    return render_template('contact.html', form=form)


@app.route('/feedback/', methods=["GET", "POST"])
def message():
    global current_page
    current_page = "feedback"
    form = Feedback()
    if form.is_submitted():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
            engine = create_engine(oracle_connection_string.format(

                username="PROJECT",
                password="Oracle",
                sid="XE",
                host="localhost",
                port="1521",
                database="PROJECT",
            ), echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = feedback(result['tour_name'], result['group_name'], result['feedback_message'])
            session.add(adddata)
            session.commit()
            return render_template('contactsubmit.html', result=result)

        except:
            result = request.form
            return render_template('submitfail.html', result=result)

    return render_template('feedback.html', form=form)



@app.route('/analyse',  methods=['GET', 'POST'])
def graphs():
    summer=len(db.session.query(tour).filter_by(year_category="summer tour").all())
    autumn = len(db.session.query(tour).filter_by(year_category="autumn tour").all())
    spring = len(db.session.query(tour).filter_by(year_category="spring tour").all())
    winter = len(db.session.query(tour).filter_by(year_category="winter tour").all())
    print(summer, autumn, spring, winter)

    checker1 = 0

    if summer == 0 and autumn == 0 and spring == 0 and winter == 0:
        checker1 = 1

    pie_graph1 = pie(summer, autumn, spring, winter)
    return render_template('analyse.html', plot1=pie_graph1,  checker1=checker1)

if __name__ == '__main__':
   app.run()