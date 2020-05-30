from flask import Flask, request, render_template,\
				  redirect,url_for,json


app = Flask(__name__)



@app.route('/api/<action>', methods = ['GET'])
def info(action):

	if action == 'health_indicators':
		return render_template('health_indicators.html',data = health_indicators)
	
	elif action == 'diseases':
		return render_template('diseases.html',data = diseases)
	
	elif action == 'all':
		return render_template('print.html',data = [health_indicators, diseases])
		
	else:
		return render_template('error.html', list_name_tables=['health_indicators','diseases'], action = action), 404
		
	


@app.route('/api',methods = ['POST','GET'])	
def api():
	if request.method == 'POST':

		if request.form.get('diseases') == 'Send':
			diseases['disease_name'] = request.form['disease_name']
			
		if request.form.get('health_indicators') == 'Send':
			health_indicators['gender'] = request.form['gender']
			health_indicators['age'] = request.form['age']
			health_indicators['current_smoker'] = request.form['current_smoker']
			health_indicators['glucose'] = request.form['glucose']
	
	return redirect(url_for('info', action = 'all'))



if __name__ == '__main__':
	
	health_indicators = {
		'gender': 'male',
		'age': '39',
		'current_smoker': 'yes',
		'glucose': '77'
	}

	diseases = {
		'disease_name': 'Alzheimer'
	}
	
	app.run(debug=True)