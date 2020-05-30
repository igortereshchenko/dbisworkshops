from app import db

class Customers(db.Model):
	__tablename__ = 'customers'

	cust_id_phone = db.Column(db.Integer, primary_key = True)
	name_cust = db.Column(db.String(100), nullable =False)
	email = db.Column(db.String(100), nullable =False), #db.CheckConstraint('email LIKE ^([a-zA-Z0-9\\-]+\\.)*[a-zA-Z0-9_\\-]+@([a-zA-Z0-9_\\-]+\\.)+(com|org|edu|net|ca|au|coop|de|ee|es|fm|fr|gr|ie|in|it|jp|me|nl|nu|ru|uk|us|za)$'))

	address_cust = db.relationship('Address', backref = 'cust_address')#, nullable = False)
	cust_orders = db.relationship('Orders', backref = 'order_cust')#, nullable = False)
	#__table_args__ = {'extend_existing': True} 


	def __init__(self, cust_id_phone, name_cust, email):
		self.cust_id_phone = cust_id_phone
		self.name_cust = name_cust
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.cust_id_phone

class Editions(db.Model):
	__tablename__ = 'editions'

	index = db.Column(db.String(100), primary_key = True)
	category = db.Column(db.String(100), nullable =False)
	edition_name = db.Column(db.String(200), nullable =False)
	price =db.Column(db.Float, db.CheckConstraint('price>0.0'))#, name = 'check_price'))
	details = db.Column(db.String(500), nullable =False)
	#__table_args__ = {'extend_existing': True} 

	ed_orders = db.relationship('Orders', backref = 'orders_ed')#, nullable = False)

	def __init__(self, index, category, edition_name, price, details):
		self.index = index
		self.category = category
		self.edition_name = edition_name
		self.price = price
		self.details = details

	def __repr__(self):
		return '<User %r>' % self.index

class Address(db.Model):
	__tablename__ = 'address'

	index = db.Column(db.String(50), primary_key = True)
	custID = db.Column(db.Integer, db.ForeignKey('customers.cust_id_phone'))
	#region = db.Column(db.String(100))
	#district = db.Column(db.String(100))
	street = db.Column(db.String(100), primary_key = True)
	houseNumber = db.Column(db.String(100), primary_key = True)

	__table_args__ = {'extend_existing': True} 
	#customers = db.relationship('Customers', backref = 'address', nullable = False)

	def __init__(self, index, custID, street, houseNumber):
		self.index = index
		self.custID = custID
		self.street = street
		self.houseNumber = houseNumber

	def __repr__(self):
		return '<User %r>' % self.index

class Orders(db.Model):
	__tablename__ = 'orders'

	id_order = db.Column(db.String(50), primary_key = True)
	edIndex = db.Column(db.Integer, db.ForeignKey('editions.index'))
	custId = db.Column(db.Integer, db.ForeignKey('customers.cust_id_phone'))
	period = db.Column(db.Integer, db.CheckConstraint('period>=1'))#, name = 'check_period'))
	quantity = db.Column(db.Integer, db.CheckConstraint('quantity>=1'))#, name = 'check_quantity'))
	order_date = db.Column(db.Date)
	totalCost = db.Column(db.Float)
	#__table_args__ = {'extend_existing': True} 


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
#db.create_all()
