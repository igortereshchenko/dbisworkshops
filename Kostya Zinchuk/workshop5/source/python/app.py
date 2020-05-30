from flask import Flask, render_template,redirect, request, url_for, g
from distionaries import user_dict, book_dict
from sqlalch.db_conn import engine
from sqlalchemy.orm import sessionmaker
from sqlalch.forms import *
import datetime
import plotly.express as px
import pandas as pd
import json
import numpy as np
import plotly.graph_objs as go
import plotly

Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)
user_log = False
user_name = ''


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/form_login', methods=['GET','POST'])
def handle():
    if request.method == 'POST':
        email = request.form['email']
        psw = request.form['password']
        global user_name
        user_name = email
        try:
            view = session.query(User).filter_by(email=email, password=psw).all()
            if view:
                global user_log
                user_log = True
                return redirect(url_for('api_action', action='home'))
            else:
                return redirect(url_for('api_action', action='home'))
        except:
            return redirect(url_for('api_action', action='home'))


@app.route('/rgs', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        login = request.form['login']
        psw = request.form['password']
        date = datetime.datetime.now()
        new_user = User.add_user(name, last_name, email, date, login, psw, 1)
        session.commit()
        return redirect(url_for('api_action', action="login"))
    return redirect(url_for('api_action', action="rgs"))


@app.route('/logout')
def logout():
    global user_log
    user_log = False
    return redirect(url_for('api_action', action="home"))


@app.route('/profile')
def profile():
    package = session.query(User).filter_by(email=user_name).first()
    return render_template('user.html', info=package, login=user_log)


def plot():
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe

    data = [
        go.Bar(
            x=df['x'],  # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def create_pie():
    a = session.query(User).filter_by(user_name='Kostya').all()
    b = session.query(User).filter(User.user_name == 'zxc').all()
    tmp_a = 0
    for _ in a:
        tmp_a += 1
    tmp_b = 0
    for _ in b:
        tmp_b += 1
    graph_values = [{
        'labels': ["Kostya", "zxc"],
        'values': [tmp_a, tmp_b],
        'type' : 'pie',
        'insidetextfont': {'color': '#FFFFFF',
                           'size': '12',
                           },
        'textfont': {'color': '#FFFFFF',
                     'size': '12',
                     },
    }]
    layout = {
        'title': '<b>Different name among all users</b>',
    }
    return graph_values, layout


@app.route('/graph1')
def graph1():
    values, layout = create_pie()
    return render_template('graph1.html', graph_values = values, layout =layout, login=user_log)


@app.route('/graph2')
def graph2():
    bar = plot()
    return render_template('graph2.html', plot=bar, login=user_log)

@app.route('/<action>/')
def api_action(action):
    if action == "book":
        return render_template('book.html', book=book_dict)
    elif action == "user":
        return render_template('user.html', user=user_dict)
    elif action == "home":
        return render_template('index.html', login=user_log)
    elif action == "login":
        return render_template('login.html')
    elif action == "rgs":
        return render_template('registration.html')
    elif action == "graph1":
        return render_template('graph1.html')
    elif action == "graph2":
        return render_template('graph2.html')
    else:
        return render_template('404.html')


@app.errorhandler(404)
def page404(error):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True)
