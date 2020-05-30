import json
import plotly
import pickle
import numpy as np
import plotly.graph_objs as go
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, request
from forms.wtf_form import  GetHealsParamForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ThisIam'


def create_pie(x1, x2):

    labels = ['гірший','кращий'] 
    values = [x1, x2]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
    	hole=.3, marker_colors=['rgb(0,255,255)','rgb(64,224,208)'])])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON




@app.route('/', methods=['GET', 'POST'])
def form():

	form = GetHealsParamForm()

	if form.validate_on_submit():

		gender = {'male': 1, 'female': 0}
		education = { 'SHS': 1, 'HSoH': 2, 'SCoVS': 3, 'U': 4 }
		agrement = {'y': 1, 'n': 0}

		args = request.form.to_dict()
		for key, value in args.items():
			if key in ['gender']:
				args[key] = gender[value] 

			elif key in ['education']:
				args[key] = education[value]

			elif key in ['smoker', 'blood_pressure', 'prevalent_stroke', 
						 'prevalent_stroke', 'prevalent_hyp', 'diabetes']:
				args[key] = agrement[value] 

		x = np.array(list(args.values())[1:]).astype(np.float)
		with open('ML/model', 'rb') as f:
			model = pickle.load(f)

		result = model.predict_proba(x.reshape(1, -1))[0][0]

		data = np.genfromtxt('ML/plotly_data.csv',delimiter=',')
		x, y = np.sum(data[:, 0] > result), np.sum(data[:, 0] < result)
		pie_graph = create_pie(x, y)


		return render_template('result.html', result=round(result, 3), 
			plot = pie_graph)

	return render_template('index.html', form=form)



if __name__ == '__main__':
	app.run(debug = True)