from flask import Flask
from flask import request
from flask import render_template

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup import user_database, todolist
import sqlalchemy

from forms.forms import SignUpForm, CreateTask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pasha'


@app.route("/", methods = ['GET'])
def hello():
  return (
	{
	  "uri": "/",
	  "sub_uri":{
			"user signup":"/signup",
			"todolist creating":"/todo",

		  }
	}
  )


@app.route('/signup', methods=["GET", "POST"])
def signup():
	form = SignUpForm()
	if form.is_submitted():
		#try:
		oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

		engine = create_engine( oracle_connection_string.format(

		username="SYSTEM",
		password="oracle",
		sid="XE",
		host="localhost",
		port="1521",
		database="PROJECT",
		), echo=True)

		Session = sessionmaker(bind=engine)
		session = Session()

		result = request.form
		adddata = user_database(result['user_name'], result['user_mail'], result['user_age'], result['login'], result['user_pass'])
		session.add(adddata)
		session.commit()
		return render_template('confirmIsOkey.html', result = result)

		#except:
		#	result = request.form
		#	return render_template('confirmIsNotOkey.html', result = result)
		
	return render_template('signup.html', form = form)


@app.route('/todo', methods=["GET", "POST"])
def todotask():
	form = CreateTask()
	if form.is_submitted():
		#try:
		oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
		engine = create_engine( oracle_connection_string.format(

		username="SYSTEM",
		password="oracle",
		sid="XE",
		host="localhost",
		port="1521",
		database="PROJECT"),
		echo=True)

		Session = sessionmaker(bind=engine)
		session = Session()

		result = request.form
		adddata = todolist(result['user_id'], result['todolist_name'], result['description_of_todo'], result['time_creating'], 1)
		session.add(adddata)
		session.commit()
		return render_template('confirmIsOkey.html', result = result)

		#except:
		#	result = request.form
		#	return render_template('confirmIsNotOkey.html', result = result)
		
	return render_template('todo.html', form = form)


if __name__ == "__main__":
	app.run(debug = True)