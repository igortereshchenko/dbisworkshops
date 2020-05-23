from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, orm, Text
from .base import AppBase, DbTools


class UserPost(AppBase, DbTools):
    __tablename__ = 'user_post'

    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    last_update = Column(DateTime)
    price = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comments = orm.relationship('comments', backref="user_post", cascade="all, delete-orphan", lazy='dynamic')
