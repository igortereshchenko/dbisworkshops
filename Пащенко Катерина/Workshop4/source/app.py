from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#os.environ['APP_SETTINGS'] = "config.DevelopmentConfig"
app.config['SQLALCHEMY_DATABASE_URI'] = "oracle+cx_oracle://SYS:student1@localhost:1521/orcl?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route('/')
def start_point():
	return render_template('index.html')




class Customers(db.Model):
	__tablename__ = 'customers'

	cust_id_phone = db.Column(db.Integer, primary_key = True)
	name_cust = db.Column(db.String(100), nullable =False)
	email = db.Column(db.String(100), nullable =False)

	address_cust = db.relationship('Address', backref = 'cust_address')
	cust_orders = db.relationship('Orders', backref = 'order_cust')

	__table_args__ = {'extend_existing': True} 


	def __init__(self, cust_id_phone, name_cust, email):
		self.cust_id_phone = cust_id_phone
		self.name_cust = name_cust
		self.email = email

	def __repr__(self):
		return '<Id %r>' % self.cust_id_phone

class Editions(db.Model):
	__tablename__ = 'editions'

	edit_id = db.Column(db.Integer, primary_key = True)
	category = db.Column(db.String(100), nullable =False)
	edition_name = db.Column(db.String(200), nullable =False)
	price =db.Column(db.Float, db.CheckConstraint('price>0.0'))#, name = 'check_price'))
	details = db.Column(db.String(500))
	__table_args__ = {'extend_existing': True} 

	ed_orders = db.relationship('Orders', backref = 'orders_ed')

	def __init__(self, edit_id, category, edition_name, price, details):
		self.edit_id = edit_id
		self.category = category
		self.edition_name = edition_name
		self.price = price
		self.details = details

	def __repr__(self):
		return '<edition %r>' % self.edit_id

class Address(db.Model):
	__tablename__ = 'address'

	id_address = db.Column(db.Integer, primary_key = True)
	custID = db.Column(db.Integer, db.ForeignKey('customers.cust_id_phone'))
	region = db.Column(db.String(100))
	district = db.Column(db.String(100))
	town = db.Column(db.String(100))
	street = db.Column(db.String(100), primary_key = True)
	houseNumber = db.Column(db.String(100), primary_key = True)

	__table_args__ = {'extend_existing': True} 
	#customers = db.relationship('Customers', backref = 'address', nullable = False)

	def __init__(self, id_address, custID, street, houseNumber):
		self.id_address = id_address
		self.custID = custID
		self.street = street
		self.houseNumber = houseNumber

	def __repr__(self):
		return '<Index %r>' % self.index

class Orders(db.Model):
	__tablename__ = 'orders'

	id_order = db.Column(db.Integer, primary_key = True)
	edIndex = db.Column(db.Integer, db.ForeignKey('editions.edit_id'))
	custId = db.Column(db.Integer, db.ForeignKey('customers.cust_id_phone'))
	period = db.Column(db.Integer, db.CheckConstraint('period>=1'))#, name = 'check_period'))
	quantity = db.Column(db.Integer, db.CheckConstraint('quantity>=1'))#, name = 'check_quantity'))
	order_date = db.Column(db.Date)
	totalCost = db.Column(db.Float)
	__table_args__ = {'extend_existing': True} 


	#orders = relationship('Editions', back_populates = 'editions')
	#order_cust = db.relationship('Customers', backref = 'cust_orders')#, nullable = False)
 

	def __init__(self,id_order, edIndex, custId, period,quantity,  order_date, totalCost):
		self.id_order = id_order
		self.edIndex = edIndex
		self.custId = custId
		self.period = period
		self.quantity = quantity
		self.order_date = order_date
		self.totalCost = totalCost
	def __repr__(self):
		return '<User %r>' % self.id_order
db.create_all()


@app.route('/editions/new', methods = ['GET', 'POST'])	
def new_edition():
	if request.method == 'POST':

		
		exists_id = db.session.query(Editions.edit_id).filter_by(edit_id = request.form["Index"]).scalar() is not None 

		if (not request.form["Index"] or not request.form["Category"] or not request.form["Name"] or not request.form["Price"] or not request.form["Details"]):
			flash('Заповніть усі поля', 'error')
		elif (float(request.form["Price"]) < 0.0):
			flash("Ціна передплати на виданя має бути більше 0", 'error')
		elif exists_id:			
			flash('Видання з індексом '+str(request.form["Index"])+' існує')
		else:
			
			edition = Editions(request.form['Index'], request.form["Category"], request.form["Name"], request.form["Price"], request.form["Details"])
			db.session.add(edition)
			db.session.commit()
			flash('Видання успішно додане')
			
	return render_template('editions_add.html')


#exists = db.session.query(db.exists().where(Editions.edit_id != 37791)).scalar()






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

			#id_order = str(now.strftime("%Y-%m-%d")).split('-')
			#sum_order = db.session.query(Orders).filter_by(order_date = now.strftime("%Y-%m-%d")).all().count()
			#if sum_order != 0:

				#id_cust = (db.session.query(Orders).filter_by(order_date = now.strftime("%Y-%m-%d")).all().count())
			#else:
				#id_cust = 0

			order_id = ''.join((datetime.datetime.now().strftime("%Y-%m-%d-%H-%M").split('-')))
			#date_now = now.strftime("%Y-%m-%d")
			#date_use = TO_DATE(date_now, 'YYYY-MM-DD')
			datetime.datetime.now()


			order = Orders(order_id, int(request.form['index_ed']), int(request.form["phone"]), int(request.form["period"]), int(request.form["quantity"]),  datetime.datetime.now().date(), float(totalcost))
			
			db.session.add(customer)

			db.session.add(address)
			#db.session.commit()

			#db.session.commit()
			db.session.add(order)
			db.session.commit()
			return redirect(url_for('start_point'))

	return render_template('new_order.html')


if __name__ == '__main__':
   #db.create_all()
   app.run(debug = True)
