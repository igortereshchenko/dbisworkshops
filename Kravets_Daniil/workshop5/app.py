from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

import plotly
import plotly.graph_objs as go
import pandas as pd
import json
from sqlalchemy.orm import sessionmaker
from database_connection import engine
from models_create import Statistic

Session = sessionmaker(bind=engine)
session1 = Session()

app = Flask(__name__)
app.secret_key = 'the_codex'

''' if request.method == 'POST':
       session.pop('user_id', None)

       username = request.form['username']
       password = request.form['password']

       user = [x for x in users if x.username == username][0]
       if user and user.password == password:
           session['user_id'] = user.id
           return redirect(url_for('charts'))

       return redirect(url_for('login'))

   return render_template('log.html')'''

@app.before_request
def before_request():
    g.user = None

    if 'user_name' in session:
        user = session['user_name']
        g.user = user


@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('log.html')

@app.route('/log_handler',  methods=['GET', 'POST'])
def handler():
    if request.method == 'POST':
        session.pop('user_name', None)
        name = request.form["username"]
        pasw = request.form["password"]
        if name != 'admin' and pasw != 'admin':
            return render_template('log.html')
        else:
            session['user_name'] = name
            return redirect(url_for('charts'))



@app.route('/charts')
def charts():
    if not g.user:
        return redirect(url_for('login'))
    bar1, bar2 = create_plot()
    pie1, pie2 = pie_flask()
    return render_template('charts.html', plot=bar1, title=bar2, graph_values=pie1, layout=pie2)

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404

def create_plot():


    x = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П`ятниця', 'Субота', 'Неділя']
    y1 = []
    y2 = []
    y3 = []
    datas = session1.query(Statistic).all()
    for i in datas:
        if i.statistic_time == '8:00':
            y1.append(i.statistic_count)
        elif i.statistic_time == '14:00':
            y2.append(i.statistic_count)
        elif i.statistic_time == '18:00':
            y3.append(i.statistic_count)

    df1 = pd.DataFrame({'x': x, 'y': y1})
    df2 = pd.DataFrame({'x': x, 'y': y2})
    df3 = pd.DataFrame({'x': x, 'y': y3})


    data = [
        go.Bar(
            x=df1['x'],
            y=df1['y'],
            name='8:00'
        ),
        go.Bar(
            x=df2['x'],
            y=df2['y'],
            name='14:00'
        ),
        go.Bar(
            x=df3['x'],
            y=df3['y'],
            name='18:00'
        )
    ]

    layout = {
        'title': '<b>Кількість замовлень усього за ефірами за днями тижня</b>',
        'barmode': 'group'
    }

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON, layout

def pie_flask():
    labs = ['Понеділок', 'Понеділок', 'Понеділок', 'Вівторок', 'Вівторок', 'Вівторок', 'Середа', 'Середа', 'Середа',
            'Четвер', 'Четвер', 'Четвер', 'П`ятниця', 'П`ятниця', 'П`ятниця', 'Субота', 'Субота', 'Субота',
            'Неділя', 'Неділя', 'Неділя']
    vals = []
    datas = session1.query(Statistic).all()
    for i in datas:
        vals.append(i.statistic_count)
    graph_values = [{
                    'labels': labs,
                    'values': vals,
                    'type': 'pie',
                    'insidetextfont': {'color': '#FFFFFF',
                                        'size': '14',
                    },
                    'textfont': {'color': '#FFFFFF',
                                        'size': '14',
                    },
    }]

    layout = {
                'title': '<b>Кількість замовлень усього за днями тижня</b>',
    }

    return graph_values, layout

if __name__ == '__main__':
    app.run()
