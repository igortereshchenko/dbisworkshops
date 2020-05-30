import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
import numpy as np
import json
from flask import Flask, render_template, request
from flask import current_app as app
import plotly.figure_factory as ff
from .. import db
from ..models import Product
from ..models import User
from sqlalchemy.sql import select



@app.route('/graphs', methods=['GET'])
def table1():
    table_data = [['First name', 'Last name', 'Email']]
    dd = db.session.query(User.first_name, User.last_name, User.email)
    for row in dd:
        table_data.append([row[0], row[1], row[2]])

    fig = ff.create_table(table_data, height_constant=60)

    data = table_data[1:]
    firstnames = []
    lastnames = []
    for row in data:
        if row[1] in lastnames:
            continue
        else:
            lastnames.append(row[1])

    for row in data:
        if row[0] in firstnames:
            continue
        else:
            firstnames.append(row[0])

    values = []


    fig.update_layout(
        title_text='Users',
        height=300,
        margin={'t': 75, 'l': 50},
        yaxis={'domain': [0, .90]},
        xaxis2={'anchor': 'y2'},
        yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': ''}
    )

    graph = plotly.io.to_html(fig)
    table = graph



    table_data = [['Product', 'Price']]
    dd = db.session.query(Product.name, Product.price)
    for row in dd:
        table_data.append([row[0], row[1]])
    fig = ff.create_table(table_data, height_constant=60)

    data = table_data[1:]
    products = []
    for row in data:
        if row[0] in products:
            continue
        else:
            products.append(row[0])

    values = []


    fig.update_layout(
        title_text='Products prices',
        height=300,
        margin={'t': 75, 'l': 50},
        yaxis={'domain': [0, .45]},
        xaxis2={'anchor': 'y2'},
        yaxis2={'domain': [.6, 1], 'anchor': 'x2', 'title': ''}
    )
    products1 = []
    price = []
    for row in data:
        products1.append(row[0])
        price.append(row[1])

    fig.add_trace(go.Bar(x=products1, y=price, xaxis='x2', yaxis='y2',
                         marker=dict(color='#abcdef')))

    graph = plotly.io.to_html(fig)
    table1 = graph
    return render_template("graphs.jinja2", plot=table,bar = table1)

