from flask import Flask
from flask import request
from flask import render_template

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import user_database, user_question
import sqlalchemy

from forms.forms import SignUpForm, CreateQuestion


app = Flask(__name__)
app.config['SECRET_KEY'] = 'jinja'


@app.route("/", methods = ['GET'])
def hello():
  return (
	{
	  "uri": "/",
	  "sub_uri":{
			"user sign up":"/registration",
			"creating question":"/question",

		  }
	}
  )


@app.route('/registration', methods=["GET", "POST"])
def registration():
	form = SignUpForm()
	if form.is_submitted():
		try:
			oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

			engine = create_engine( oracle_connection_string.format(

				username="PROJECTDB",
				password="oracle123",
				sid="XE",
				host="localhost",
				port="1521",
				database="PROJECTDB",
				), echo=True)

			Session = sessionmaker(bind=engine)
			session = Session()

			result = request.form
			add_data = user_database(result['user_name'], result['user_mail'], result['user_age'], result['edrpou'], result['user_pass'])
			session.add(add_data)
			session.commit()
			return render_template('Ok.html', result = result)

		except:
			result = request.form
			return render_template('notOk.html', result = result)
		
	return render_template('user_registration.html', form = form)


@app.route('/question', methods=["GET", "POST"])
def question():
	form = CreateQuestion()
	if form.is_submitted():
		try:
			oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
			engine = create_engine(oracle_connection_string.format(

				username="PROJECTDB",
				password="oracle123",
				sid="XE",
				host="localhost",
				port="1521",
				database="PROJECTDB",
			), echo=True)

			Session = sessionmaker(bind=engine)
			session = Session()

			result = request.form
			add_data = user_question(result['user_id'], result['question_reference'], result['question'], result['time_creating'], 1)
			session.add(add_data)
			session.commit()
			return render_template('Ok.html', result = result)

		except:
			result = request.form
			return render_template('notOk.html', result = result)
		
	return render_template('question.html', form = form)


if __name__ == "__main__":
	app.run(debug = True)