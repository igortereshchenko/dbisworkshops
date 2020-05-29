from flask import Flask, render_template, request, redirect, url_for, g, session, flash
from forms import SignUpForm
from flask_bootstrap import Bootstrap

import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

import pandas as pd
import numpy as np
import random
import json

from OracleDb import OracleDb
from model import *

db = OracleDb()

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'xxsemaforxx'


@app.before_request
def before_request():
    '''
        Перед ревкестом робимо перевірку
        чи юзер зайшов чи ні
    '''
    g.user = None

    if 'user_name' in session:
        user = session['user_name']
        g.user = user


@app.route('/api/<action>', methods=['GET', 'POST'])
def apiget(action):
    '''
        Роутинг з параметрами по сайту
    '''
    if not g.user:
        return redirect(url_for('signup'))

    if action == "master":
        return render_template("master.html")

    elif action == "guide":
        return render_template("guide.html")

    elif action == "data":
        session = db.sqlalchemy_session
        all_snacks = session.query(snack).all()
        return render_template("data.html", snacks=all_snacks)

    elif action == "films":
        session = db.sqlalchemy_session
        all_films = session.query(films).all()
        return render_template("films.html", films=all_films)

    elif action == "analytics":
        bar_table1 = create_table_plot()
        bar_table2 = create_table_plot2()
        return render_template("analytics.html", plot=bar_table1, bar=bar_table2)

    else:
        return render_template("404.html", action_value=action)


@app.route('/update', methods=['GET', 'POST'])
def update():
    '''
            Функція апдейту для снеків
    '''
    if request.method == 'POST':
        session = db.sqlalchemy_session
        my_data = session.query(snack).get(request.form.get('snack_id'))

        my_data.snack_name = request.form['snack_name']
        my_data.age_limit = request.form['age_lim']
        my_data.price = request.form['price']
        my_data.orders_num = request.form['order_num']

        session.commit()

        flash("Snack Data Updated Successfully!")

        return redirect(url_for('apiget', action="data"))


@app.route('/delete/<id>', methods=['POST', 'GET'])
def delete(id):
    '''
            Функція видалення для снеків
    '''
    session = db.sqlalchemy_session
    data = session.query(snack).get(id)
    session.delete(data)
    session.commit()

    flash("Snack Deleted Successfully!")

    return redirect(url_for('apiget', action="data"))


@app.route('/insert', methods=['POST'])
def insert():
    '''
            Функція вставки для снеків
    '''
    if request.method == 'POST':
        name = request.form['snack_name']
        age_lim = request.form['age_lim']
        price = request.form['price']
        num_ord = request.form['order_num']

        new_snack = snack.add_member(name=name,
                                     price=price,
                                     orders_num=num_ord,
                                     age_limit=age_lim)

        flash('Snack inserted succesfuly!')
        return redirect(url_for('apiget', action="data"))


@app.route('/update1', methods=['GET', 'POST'])
def update1():
    '''
            Функція апдейту для фільмів
    '''
    if request.method == 'POST':
        session = db.sqlalchemy_session
        my_data = session.query(films).get(request.form.get('film_id'))

        my_data.film_name = request.form['film_name']
        my_data.age_limit = request.form['age_lim']

        session.commit()

        flash("Film Data Updated Successfully!")

        return redirect(url_for('apiget', action="films"))


@app.route('/delete1/<id>', methods=['POST', 'GET'])
def delete1(id):
    '''
            Функція удаления для фільмів
    '''
    session = db.sqlalchemy_session
    data = session.query(films).get(id)
    session.delete(data)
    session.commit()

    flash("Film Deleted Successfully!")

    return redirect(url_for('apiget', action="films"))


@app.route('/insert1', methods=['POST'])
def insert1():
    '''
            Функція вставке для фільмів
    '''
    if request.method == 'POST':
        name = request.form['film_name']
        age_lim = request.form['age_lim']

        new_snack = films.add_member(name=name,
                                     age_limit=age_lim)

        flash('Films inserted succesfuly!')
        return redirect(url_for('apiget', action="films"))


@app.route('/handle_form', methods=['GET', 'POST'])
def handler():
    '''
            Функція яка валідує форму логіну
    '''
    if request.method == 'POST':
        session.pop('user_name', None)
        name = request.form["username"]
        pasw = request.form["password"]
        if name != 'admin' and pasw != 'admin':
            return render_template('log_form.html')
        else:
            session['user_name'] = name
            return redirect(url_for('apiget', action="master"))


@app.route('/', methods=['GET', 'POST'])
def signup():
    return render_template('log_form.html')


def create_table_plot():
    '''
        Створення бар-чарту для кінотеатрів
    '''
    table_data = [['Cinema name', 'Location', 'Number of orders']]
    dd = db.execute('SELECT cinema_name, cinema_location, orders_num FROM cinema')
    for row in dd:
        table_data.append([row[0], row[1], row[2]])

    fig = ff.create_table(table_data, height_constant=60)

    data = table_data[1:]
    names = []
    cities = []
    for row in data:
        if row[1] in cities:
            continue
        else:
            cities.append(row[1])

    for row in data:
        if row[0] in names:
            continue
        else:
            names.append(row[0])

    values = []
    for i in range(len(cities)):
        per_city = []
        for row in data:
            if row[0] in names and row[1] == cities[i]:
                per_city.append(row[2])
        values.append(per_city)

        fig.add_traces([go.Bar(x=names, y=values[i], xaxis='x2', yaxis='y2',
                               marker=dict(color='#AF02FF'),
                               name='{}'.format(cities[i]))])

    fig.update_layout(
        title_text='Theatres stats',
        height=800,
        margin={'t': 75, 'l': 50},
        yaxis={'domain': [0, .45]},
        xaxis2={'anchor': 'y2'},
        yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Orders'}
    )

    graph = plotly.io.to_html(fig)

    return graph


def create_table_plot2():
    '''
        Створення бар-чарту для снеків
    '''
    table_data = [['Snack name', 'Snack price', 'Number of orders']]
    dd = db.execute('SELECT snack_name, price, orders_num FROM snack')
    for row in dd:
        table_data.append([row[0], row[1], row[2]])

    # Initialize a fig with ff.create_table(table_data)
    fig = ff.create_table(table_data, height_constant=60)

    data = table_data[1:]
    names = []
    price = []
    for row in data:
        names.append(row[0])
        price.append(row[2])

    fig.add_trace(go.Bar(x=names, y=price, xaxis='x2', yaxis='y2',
                         marker=dict(color='#FF1D84')))
    fig.update_layout(
        title_text='Snack stats',
        height=800,
        margin={'t': 75, 'l': 50},
        yaxis={'domain': [0, .45]},
        xaxis2={'anchor': 'y2'},
        yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': 'Orders'}
    )

    graph = plotly.io.to_html(fig)

    return graph


if __name__ == "__main__":
    app.run(debug=True)
