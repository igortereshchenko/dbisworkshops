from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
	Column, Integer, String, DateTime, Boolean, Text, ForeignKey
)
from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

Base = declarative_base()

class TimestampMixin:
    created = Column(
        DateTime, nullable=False, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)


class Note(TimestampMixin, Base):
	__tablename__ = 'note'
	id = Column(Integer, primary_key=True)
	url_id = Column(String(9), unique=True, nullable=False)
	title = Column(String(100))
	text = Column(Text)

	def __repr__(self):
		return '{}th note {}'.format(self.id, self.url_id)


class User(UserMixin, Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	username = Column(String(30), unique=True, nullable=False)
	email = Column(String(50))
	_password_hash = Column('password_hash', String(128), nullable=False)

	@hybrid_property
	def password_hash(self):
		return self._password_hash

	@password_hash.setter
	def password(self, password):
		self._password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self._password_hash, password)

	def __repr__(self):
		return '{}th user {}'.format(self.id, self.username)


class UserNoteParams(Base):
	__tablename__ = 'user_note_params'
	id = Column(Integer, primary_key=True)
	note_id = Column(Integer, ForeignKey('note.id'))
	user_id = Column(Integer, ForeignKey('user.id'))
	change_possibility = Column(Boolean)
	private_access = Column(Boolean)
	encryption = Column(Boolean)
	# one to one
	user = relationship('User', backref=backref('user_note_params'), uselist=False)
	# many to one
	note = relationship('Note', backref='user_note_params')


class PrivateAccess(Base):
	__tablename__ = 'private_access'
	id = Column(Integer, primary_key=True)
	note_id = Column(Integer, ForeignKey('note.id'))
	user_id = Column(Integer, ForeignKey('user.id'))
	# many to one
	user = relationship('User', backref='private_accesses')
	# one to one
	note = relationship('Note', backref=backref('private_access'), uselist=False)

