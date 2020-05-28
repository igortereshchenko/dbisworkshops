import pickle
import numpy as np
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import sessionmaker

from forms.wtf_form import  GetHealsParamForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ThisIam'



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

		result = model.predict_proba(x.reshape(1, -1))

		return render_template('result.html', result=round(result[0][0], 3))

	return render_template('index.html', form=form)


@app.route('/result')
def result():
	return render_template('result.html')


if __name__ == '__main__':
	app.run(debug = True)