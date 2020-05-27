from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
#from db_connection import engine
#from ORM_relations import Editions

import os

app = Flask(__name__)

os.environ['APP_SETTINGS'] = "config.DevelopmentConfig"
os.environ['DATABASE_URL'] = "oracle+cx_oracle://SYS:student1@localhost:1521/orcl?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true"

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)
from models import Customers




#app.config['SECRET_KEY'] = "random string"

@app.route('/')
def start_point():
	return render_template('index.html')

@app.route('/editions/new', methods = ['GET', 'POST'])	
def new_edition():
	if request.method == 'POST':
		if (not request.form["Index"] or not request.form["Category"] or not request.form["Name"] or not request.form["Price"] or not request.form["Details"]):
			flash('Заповніть усі поля', 'error')
		elif (float(request.form["Price"]) < 0.0):
			flash("Ціна передплати на виданя має бути більше 0", 'error')
		elif (int(request.form["Index"]) == int(db.session.query(Editions).filter_by(index = request.form["Index"]).first().index)):
			flash('Видання з індексом '+str(request.form["Index"])+' існує')
		else:
			edition = Editions(request.form['Index'], request.form["Category"], request.form["Name"], request.form["Price"], request.form["Details"])
			db.session.add(edition)
			db.session.commit()
			flash('Видання успішно додане')
			return redirect(url_for('start_point'))
	return render_template('editions_add.html')

from datetime import datetime
import datetime

@app.route('/editions/order', methods = ['GET', 'POST'])
def new_order():
	if request.method == 'POST':
		if int(request.form["period"])<=0:
			flash("Мінімальний період передплати ставновить 1 місяць")
		elif int(request.form["quantity"])<=0:
			flash("Мінімальна кількість екземплярів - 1 екземпляр")
		
		else:
			customer = Customers(int(request.form["phone"]), request.form["name"],  request.form["email"])


			address = Address(int(request.form["index"]), int(request.form["phone"]),   request.form["street"],  request.form["houseNumber"])


			totalcost = int(request.form["period"])*float(db.session.query(Editions).filter_by(index = request.form["index_ed"]).first().price)

			

			order_id = ''.join((datetime.datetime.now().strftime("%Y-%m-%d-%H-%M").split('-')))
			
			datetime.datetime.now()


			order = Orders(order_id, int(request.form['index_ed']), int(request.form["phone"]), int(request.form["period"]), int(request.form["quantity"]),  datetime.datetime.now().date(), float(totalcost))
			
			db.session.add(customer)
			db.session.add(address)
			db.session.add(order)
			db.session.commit()
			return redirect(url_for('start_point'))

	return render_template('new_order.html')


if __name__ == '__main__':
   app.run(debug = True)
