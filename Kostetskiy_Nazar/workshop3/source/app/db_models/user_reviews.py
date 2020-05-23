from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from .base import AppBase, DbTools
from flask_login import UserMixin


# Відгуки про користувача, де reviewer_id - ідентифікатор комментатора
class UserReviews(AppBase, DbTools, UserMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    text = Column(String)
    rating = Column(Integer(), CheckConstraint('0 <= rating <= 100', name='rat_constr'), nullable=False)
