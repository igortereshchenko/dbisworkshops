from flask import Flask, render_template, request
from forms import UserForm
import plotly
import plotly.graph_objs as go

import pandas as pd
import json

from database_connection import engine
from sqlalchemy.orm import sessionmaker
from model import Payed

Session = sessionmaker(bind=engine)
session = Session()


def create_plot():
    a = session.query(Payed).order_by(Payed.payment_time).all()
    d = []
    w = []
    p = []
    g = []
    for i in a:
        date = i.payment_time.date()
        d.append("{0} {1}".format(date.day, ["січня", "лютого", "березня", "квітня", "травня", "червня", "липня",
                                "серпня", "вересня", "жовтня", "листопада", "грудня"][int(date.month) - 1]))
        w.append(i.water_payed)
        p.append(i.power_payed)
        g.append(i.gas_payed)

    water_df = pd.DataFrame({'x': d, 'y': w})
    power_df = pd.DataFrame({'x': d, 'y': p})
    gas_df = pd.DataFrame({'x': d, 'y': g})

    data = [
        go.Bar(
            x=water_df['x'],
            y=water_df['y'],
            name='Водопостачання'

        ),
        go.Bar(
            x=gas_df['x'],
            y=gas_df['y'],
            name='Газопостачання'
        ),
        go.Bar(
            x=power_df['x'],
            y=power_df['y'],
            name='Електропостачання'
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def create_pie():
    a = session.query(Payed).all()
    wp = 0
    gp = 0
    pp = 0
    for i in a:
        wp += i.water_payed
        gp += i.gas_payed
        pp += i.power_payed

    graph_values = [{
        'labels': ["Водопостачання", "Газопостачання", "Електропостачання"],
        'values': [wp, gp, pp],
        'type': 'pie',
        'insidetextfont': {'color': '#FFFFFF',
                           'size': '14',
                           },
        'textfont': {'color': '#FFFFFF',
                     'size': '14',
                     },
    }]
    layout = {
        'title': '<b>Відсоток сплат за послуги</b>',

    }
    return graph_values, layout

data = {}
data['admin'] = {
    "login": "admin",
    "password": "admin"
}
logged = 0


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sd315g566adw'


@app.route('/', methods=['GET', 'POST'])
def index():
    global logged
    print(logged)
    if logged == 0:
        form = UserForm()
        if form.is_submitted():
            result = request.form
            if result['username'] == data['admin']['login'] and result['password'] == data['admin']['password']:
                logged = 1
                bar = create_plot()
                values, layout = create_pie()
                return render_template('stats.html', plot=bar, graph_values=values, layout=layout, logged=logged)
        return render_template('user.html', form=form)
    else:
        bar = create_plot()
        values, layout = create_pie()
        return render_template('stats.html', plot=bar, graph_values=values, layout=layout, logged=logged)



@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)