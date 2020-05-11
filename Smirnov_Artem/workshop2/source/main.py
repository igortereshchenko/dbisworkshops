from flask import Flask, request, render_template,\
				  redirect,url_for,json


app = Flask(__name__)

student_dict = {
		'student_name': 'BIb',
		'student_age': '228'
	}

univer_dict = {
		'univer_name': 'KPI',
		'univer_city': 'Kiev'
	}

@app.route('/api/<action>', methods=['GET'])
def get_info(action):
	if action == 'student':
		return render_template('student.html',data = student_dict)
	
	elif action == 'university':
		return render_template('univer.html',data = univer_dict)
	
	elif action == 'all':
		return render_template('all.html',data = [student_dict,univer_dict])
		
	else:
		return render_template('error.html',
								list_name_tables=['student','university'],
								action=action),404
		
	

# @app.route('/', methods=['POST','GET'])
@app.route('/api',methods=['POST','GET'])	
def api():
	if request.method == 'POST':

		if request.form.get('univer') == 'Send':
			univer_dict['univer_name'] = request.form['univer_name']
			univer_dict['univer_city'] = request.form['univer_city']
			
		if request.form.get('student') == 'Send':
			student_dict['student_name'] = request.form['student_name']
			student_dict['student_age'] = request.form['student_age']
	
	return redirect(url_for('get_info',action='all'))



if __name__ == '__main__':
	
	
	app.run(debug=True)