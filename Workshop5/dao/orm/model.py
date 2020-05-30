from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class ormUser(Base):
    __tablename__ = 'user_table'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(15), nullable=False)
    user_surname = Column(String(20), nullable=False)
    user_email = Column(String(50), unique=True, nullable=False)
    user_phone = Column(String(15), unique=True)
    user_password = Column(String(60), nullable=False)
    end_date = Column(Date)

    orm_token = relationship('ormToken', secondary='user_token')


class ormToken(Base):
    __tablename__ = 'token'
    token_id = Column(Integer, primary_key=True)
    user_token = Column(String(253))

    orm_user = relationship('ormUser', secondary='user_token')

class ormUserToken(Base):
    __tablename__ = 'user_token'

    user_table_user_id = Column(Integer, ForeignKey('user_table.user_id'), primary_key=True)
    token_token_id = Column(Integer, ForeignKey('token.token_id'), primary_key=True)
