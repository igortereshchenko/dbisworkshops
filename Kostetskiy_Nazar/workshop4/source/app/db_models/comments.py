from sqlalchemy import Column, Integer, ForeignKey, Text

from .base import AppBase, DbTools


class Comments(AppBase, DbTools):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    text = Column(Text, nullable=False)
    # Defining the Foreign Key on the Child Table
    post_id = Column(Integer, ForeignKey('user_post.id'), nullable=False)
