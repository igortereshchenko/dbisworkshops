from sqlalchemy import Column, Integer, String
from .base import AppBase, DbTools
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(AppBase, DbTools, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(), nullable=False)
    phone = Column(String(30))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_data(self):
        return {'user_id': self.id, 'username': self.username, 'email': self.email}


