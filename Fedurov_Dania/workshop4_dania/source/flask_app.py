from flask import Flask
from flask import request
from flask import render_template

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import user_database, prediction_database, numerology_database
import sqlalchemy

from forms.forms import User_registration, Add_prediction, Add_numerology_date


app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask'


@app.route("/", methods = ['GET'])
def hello():
  return (
	{
	  "uri": "/",
	  "sub_uri":{
			"user registrarion":"/registration",
			"create prediction":"/prediction",
			"create numerologic":"/numerologic"

		  }
	}
  )


@app.route('/registration', methods=["GET", "POST"])
def registration():
	form = User_registration()
	if form.is_submitted():
		try:
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
			add = user_database(result['user_name'], result['user_surname'], result['user_age'], result['user_mail'], result['user_login'], result['user_pass'])
			session.add(add)
			session.commit()
			return render_template('Ok.html', result = result)

		except:
			result = request.form
			return render_template('notOk.html', result = result)
		
	return render_template('registration_of_user.html', form = form)


@app.route('/prediction', methods=["GET", "POST"])
def prediction():
	form = Add_prediction()
	if form.is_submitted():
		try:
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
			adddata = prediction_database(result['prediction_description'])
			session.add(adddata)
			session.commit()
			return render_template('Ok.html', result = result)

		except:
			result = request.form
			return render_template('notOk.html', result = result)
		
	return render_template('prediction.html', form = form)


@app.route('/numerologic', methods=["GET", "POST"])
def numerologic():
	form = Add_numerology_date()
	if form.is_submitted():
		try:
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
			adddata = numerology_database(result['numerology_date'], result['numerology_description'])
			session.add(adddata)
			session.commit()
			return render_template('Ok.html', result = result)

		except:
			result = request.form
			return render_template('notOk.html', result = result)
		
	return render_template('numerology.html', form = form)

if __name__ == "__main__":
	app.run(debug = True)