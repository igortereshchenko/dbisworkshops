from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB_URL = 'postgresql+psycopg2://{user}:{pw}'.format(user='me',pw='Mara8150684')
app.config['SQLALCHEMY_DATABASE_URL'] = "postgresql://postgres@localhost/votingApp"

db = SQLAlchemy(app)

from models import Deputee, Project
from flask import render_template, url_for, abort, request, redirect

from datetime import datetime


@app.route('/')
def welcome():
	return render_template('welcome.html', time=datetime.now().strftime("%H:%M:%S"))

@app.route('/api/<action>', methods=['POST', 'GET'])
def action(action=None):
	if action=="deputee":
		return render_template('deputee.html', dictionary=deputee)
	elif action=="project":
		return render_template('project.html', dictionary=project)
	elif action=="all":
		if request.method=='POST':
			result = request.form
			if 'password' in list(result.keys()):
				deputee['name'] = result['name']
				deputee['face'] = result['face']
				deputee['password'] = result['password']
				deputee['head'] = result['head']
				deputee['fraction'] = result['fraction']
				deputee['mobile'] = result['mobile']
			else:
				project['name'] = result['name']
				project['date_added'] = result['date_added']
				project['document'] = result['document']
				project['author'] = result['author']
				project['deadline'] = result['deadline']
			
			return redirect(url_for('action', action="all"))
		return render_template('all.html', dictProj=project, dictDep=deputee)
	else:
		abort(404)
	


if __name__=='__main__':
	deputee = { "name":"Микола Старицький",
				"face":[],
				"password":"******",
				"head":1,
				"fraction":"Свобода",
				"mobile":"+380829562957"}
	project = { "name":"Авторське право",
				"date_added":"26.05.20",
				"document":"law1.pdf",
				"author":"Микола Старицький",
				"deadline":"5.06.20"}
	app.run(debug=True)