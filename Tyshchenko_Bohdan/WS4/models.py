from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from app import db

class Deputee(db.Model):
	__table_args__ = {'extend_existing': True} 
	name = db.Column(db.String(128), primary_key=True)
	face = db.Column(db.String(64), index=True, unique=True)
	password = db.Column(db.String(32))
	password_hash = db.Column(db.String(128))
	head = db.Column(db.Integer)
	fraction = db.Column(db.String(140))
	mobile = db.Column(db.String(20), primary_key=True)
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	
		
class Project(db.Model):
	__table_args__ = {'extend_existing': True} 
	name = db.Column(db.Integer, primary_key=True)
	date_added = db.Column(db.DateTime, default=datetime.utcnow)
	document = db.Column(db.String(120), index=True, unique=True)
	author = db.Column(db.String(128), db.ForeignKey('deputee.name'))
	deadline = db.relationship('Post', backref='author', lazy='dynamic')