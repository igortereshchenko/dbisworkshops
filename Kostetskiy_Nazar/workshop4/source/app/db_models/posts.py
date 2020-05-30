from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float, orm, Text
from .base import AppBase, DbTools


class UserPost(AppBase, DbTools):
    __tablename__ = 'user_post'

    id = Column(Integer, primary_key=True)
    position = Column(Text)
    body = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    last_update = Column(DateTime)
    price_usd = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comments = orm.relationship('Comments', backref="post")
