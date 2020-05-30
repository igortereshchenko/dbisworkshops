from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os
import re
from datetime import datetime
import datetime
import random
import json
import plotly
import numpy as np
import plotly.graph_objs as go

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "oracle+cx_oracle://SYS:student1@localhost:1521/orcl?encoding=UTF-8&nencoding=UTF-8&mode=SYSDBA&events=true"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)



class Customers(db.Model):
	__tablename__ = 'customers'

	cust_id = db.Column(db.String(50), primary_key = True)
	name_cust = db.Column(db.String(100), nullable =False)
	cust_phone = db.Column(db.Integer, nullable = False)
	email = db.Column(db.String(100), nullable =False)

	address_cust = db.relationship('Address', backref = 'cust_address')
	cust_orders = db.relationship('Orders', backref = 'order_cust')

	__table_args__ = {'extend_existing': True} 


	def __init__(self, cust_id, name_cust,cust_phone,  email):
		self.cust_id = cust_id
		self.cust_phone = cust_phone
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


	address_id = db.Column(db.String(50), primary_key = True)
	address_index = db.Column(db.String(50), primary_key = True)
	cust_id = db.Column(db.String(50), db.ForeignKey('customers.cust_id'))
	region = db.Column(db.String(100))
	district = db.Column(db.String(100))
	town = db.Column(db.String(100))
	street = db.Column(db.String(100), primary_key = True)
	houseNumber = db.Column(db.String(100), primary_key = True)

	__table_args__ = {'extend_existing': True} 
	#customers = db.relationship('Customers', backref = 'address', nullable = False)

	def __init__(self,address_id,   address_index, cust_id, region, district, town, street, houseNumber):
		self.address_id = address_id
		self.address_index = address_index
		self.cust_id = cust_id
		self.region = region
		self.district = district
		self.town = town
		self.street = street
		self.houseNumber = houseNumber

	def __repr__(self):
		return '<Index %r>' % self.index

class Orders(db.Model):
	__tablename__ = 'orders'

	id_order = db.Column(db.String(50), primary_key = True)
	ed_index = db.Column(db.Integer, db.ForeignKey('editions.edit_id'))
	cust_id = db.Column(db.String(50), db.ForeignKey('customers.cust_id'))
	period = db.Column(db.String(100), db.CheckConstraint('period>=1'))#, name = 'check_period'))
	quantity = db.Column(db.Integer, db.CheckConstraint('quantity>=1'))#, name = 'check_quantity'))
	order_date = db.Column(db.String(50))
	total_cost = db.Column(db.Float)
	__table_args__ = {'extend_existing': True} 
 
	def __init__(self,id_order, ed_index, cust_id, period,quantity,  order_date, total_cost):
		self.id_order = id_order
		self.ed_index = ed_index
		self.cust_id = cust_id
		self.period = period
		self.quantity = quantity
		self.order_date = order_date
		self.total_cost = total_cost
	def __repr__(self):
		return '<User %r>' % self.id_order

db.create_all()




@app.route('/', methods = ['GET', 'POST'])
def start_point():
	gsearch = request.args.get('gsearch')
	check_int = re.fullmatch('^\\d*$', str(gsearch))# identidication integer or strin
	find_id = "Пошук - "+str(gsearch)
	if gsearch:
		if check_int:
			exists_id = db.session.query(Editions.edit_id).filter_by(edit_id = int(gsearch)).scalar() is not None 
			if exists_id:
				editions = db.session.query(Editions).filter_by(edit_id = int(gsearch)).all()
				return render_template('find_index.html', editions = editions, find_id = find_id)
			else:
				error = "Видання не знайдено"
				return render_template('error_massage.html', error_massage = error, find_id = find_id )
		else:
			exists_id = db.session.query(Editions.edition_name).filter_by(edition_name = gsearch).scalar() is not None 
			if exists_id:
				editions = db.session.query(Editions).filter_by(edition_name = gsearch).all()
				return  render_template('find_index.html', editions = editions, find_id = find_id)
			else: 
				error = "Видання не знайдено"
				return render_template('error_massage.html', error_massage = error, find_id = find_id )
	else:

		popular_editions = db.session.query(Editions).filter_by(category = 'Популярні видання').all()
		return render_template('index.html', editions = popular_editions, category = 'Популярні видання')



def create_pie(x1, x2):

	labels = ['Підтверджено','Скасовано'] 
	values = [x1, x2]

	fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', hole=.3, marker_colors=['rgb(0,255,255)','rgb(64,224,208)'])])
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

	return graphJSON

@app.route('/plot')
def plot():
	x = db.session.query(Editions.category).all()
	y = len(db.session.query(Editions.category).all())
	pie_graph = create_pie(x, y)
	return render_template('plot_my.html', plot = pie_graph)
	




@app.route('/category', methods = ["POST", "GET"])
def show_category():
	if request.method == "POST":
		select_categ = request.form.get('select_categ')
		sort_categ = request.form.get('sort_categ')
		if select_categ == "Всі категорії" and sort_categ:
			return redirect(url_for('start_point'))

		elif select_categ != "Всі категорії" and sort_categ == "за замовчуванням":
			editions_categ = db.session.query(Editions).filter_by(category = select_categ)
			return render_template('show_category.html', select_categ = select_categ, editions_categ = editions_categ, type_sort = sort_categ )

		else:
			if select_categ != "Всі категорії" and sort_categ == "назва(А-Я)":
				editions_categ = db.session.query(Editions).filter_by(category = select_categ).order_by(Editions.edition_name).all()
				sort_type = sort_categ

			elif select_categ != "Всі категорії" and sort_categ == "назва(Я-А)":
				editions_categ = db.session.query(Editions).filter_by(category = select_categ).order_by(Editions.edition_name.desc()).all()
				sort_type = sort_categ

			elif select_categ != "Всі категорії" and sort_categ == "ціна(за зростанням)":
				editions_categ = db.session.query(Editions).filter_by(category = select_categ).order_by(Editions.price).all()
				sort_type = sort_categ

			elif select_categ != "Всі категорії" and sort_categ == "ціна(за зменшенням)":
				editions_categ = db.session.query(Editions).filter_by(category = select_categ).order_by(Editions.price.desc()).all()
				sort_type = sort_categ

			elif select_categ != "Всі категорії" and sort_categ == "індекс видання(А-Я)":
				editions_categ = db.session.query(Editions).filter_by(category = select_categ).order_by(Editions.edit_id).all()
				sort_type = sort_categ
			elif select_categ != "Всі категорії" and sort_categ == "індекс видання(Я-A)":
				editions_categ = db.session.query(Editions).filter_by(category = select_categ).order_by(Editions.edit_id.desc()).all()
				sort_type = sort_categ
		return render_template('show_category.html', select_categ = select_categ, editions_categ = editions_categ, type_sort = sort_categ)



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



@app.route('/new_order', methods = ['GET', 'POST'])
def start_order():
	if request.method == 'POST':
		id_new_order_edit = request.form.get('id_new_order_edit')
		edition = db.session.query(Editions).filter_by(edit_id = id_new_order_edit).first()
		#period_list = request.form.getlist('datecheckbox')
		return render_template('test_form.html',edition = edition)
	return render_template('index.html')



@app.route('/user_info', methods = ['GET', 'POST'])
def user_info():
	if request.method == "POST":
		id_new_order_edit = request.form.get('id_new_order_edit')
		edition = db.session.query(Editions).filter_by(edit_id = id_new_order_edit).first()

		period = request.form.getlist('datecheckbox')

		if len(period)==0:
			flash("Мінімальний період передплати - 1 місяць")
			return render_template('test_form.html', edition = edition)

		else:
			quatity_months = len(period)
			period = '/'.join(period)
			quantity = request.form.get('num')
			total_cost = int(quantity)*quatity_months*float(edition.price)
			return render_template('user_infor.html', edition=edition, period = period, quantity = quantity, total_cost = total_cost)
	return render_template('test_form.html')



@app.route('/confirm_order', methods = ['GET', 'POST'])
def confirm_address():
	if request.method == "POST":
		index_edition = request.form.get('index')
		quantity = request.form.get('quantity')
		period = request.form.get('period')
		edition = db.session.query(Editions).filter_by(edit_id = index_edition).first()
		total_cost = request.form.get('total_cost')

		cust_name = request.form.get('name')
		cust_phone = request.form.get('phone')
		cust_email = request.form.get('email')

		address_index = request.form.get('town_index')
		address_region = request.form.get('region')
		address_dist =request.form.get('district')
		address_town = request.form.get('town')
		address_street = request.form.get('street')
		address_num = request.form.get('houseNumber')


		if (not cust_name) or (not cust_phone) or( not cust_email) or (not address_index) or (not address_street) or (not address_num):
			flash("Всі поля * мають бути заповнені")
			return render_template('user_infor.html', edition=edition, period = period, quantity = quantity, total_cost = total_cost, cust_name = cust_name,cust_phone = cust_phone, cust_email = cust_email, address_index = address_index, address_region = address_region, address_dist = address_dist, address_town = address_town, address_num = address_num  )
		else:

			template_id = ''.join((datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S").split('-')))[2:]
			cust_id = str(template_id)+str(random.randint(0, 9))+str(random.randint(0, 9))

			customer = Customers(cust_id, cust_name, cust_phone, cust_email)

			address_id = template_id+str(random.randint(0, 9))+str(random.randint(0, 9))
			adsress = Address(address_id, address_index, cust_id, address_region , address_dist, address_town, address_street, address_num)

			order_id = template_id+str(random.randint(0, 9))+str(random.randint(0, 9))

			date_now = datetime.datetime.now().strftime("%d-%m-%Y")
			#data_list = date_now.split('-')
			#x = datetime.date(int(data_list[0]), int(data_list[1]), int(data_list[2]))

			order = Orders(order_id, int(index_edition), cust_id, period, int(quantity), date_now, total_cost)

			db.session.add(customer)

			db.session.add(adsress)

			db.session.add(order)
			db.session.commit()

			return render_template("success.html", id_order = order_id )
	return render_template('user_infor.html')







if __name__ == '__main__':
   #db.create_all()
   app.run(debug = True)


