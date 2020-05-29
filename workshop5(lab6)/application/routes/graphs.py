import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
import numpy as np
import json
from flask import Flask, render_template, request
from flask import current_app as app



@app.route('/graphs', methods=['GET'])
def graphs():
    count = 500
    x = np.linspace(-np.pi, np.pi, 50)
    y = np.sin(x)


    line = go.Scatter(
        x=x,
        y=y,
        name="sin(x)"
    )

    bar = go.Bar(
        x=["Product","Price"],
        y=[50,100]
    )
    data = [line,bar]
    ids=[1,2]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('graphs.jinja2',
                           graphJSON=graphJSON, ids=ids)
