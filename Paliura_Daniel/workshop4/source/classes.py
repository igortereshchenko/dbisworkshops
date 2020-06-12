from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, or_
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash
from datetime import datetime

from oracledb import *


Base = declarative_base()
db = OracleDb()


class User(Base):
    __tablename__ = 'USERS'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    last_name = Column(String(55), nullable=True)
    lang_code = Column(String(5), nullable=False)
    username = Column(String(45), nullable=False, unique=True)
    password = Column(String(140), nullable=False)
    reg_date = Column(DateTime, nullable=False)

    dialogs_initiated = relationship("Dialog", back_populate="initiator")
    dialogs_as_target = relationship("Dialog", back_populate="target")
    messages_sent = relationship("Message", back_populate="sender")
    messages_received = relationship("Message", back_populate="receiver")


    @classmethod
    def add_user(cls, name, lang_code, username, password, last_name=None, reg_date=datetime.utcnow()):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = cls(
            name=name,
            last_name=last_name,
            lang_code=lang_code,
            username=username,
            password=generate_password_hash(password),
            reg_date=reg_date
        )
        session.add(new_user)
        session.commit()


class Dialog(Base):
    __tablename__ = 'DIALOGS'
    id = Column(Integer, primary_key=True)
    initiator_id = Column(Integer, ForeignKey("USERS.id"))
    target_id = Column(Integer, ForeignKey("USERS.id"))

    initiator = relationship("User", back_populate="dialogs_initiated")
    target = relationship("User", back_populate="dialogs_as_target")
    messages = relationship("Message", back_populates='dialog')


    @classmethod
    def add_dialog(cls, initiator_id, target_id):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_dialog = cls(
            initiator_id=initiator_id,
            target_id=target_id
        )
        session.add(new_dialog)
        session.commit()


    @classmethod
    def get_user_dialogs(cls, user_id):
        return session.query(cls).filter(or_(cls.initiator_id == user_id, cls.target_id == user_id))


class Message(Base):
    __tablename__ = 'MESSAGES'

    date = Column(DateTime, nullable=False)
    dialog_id = Column(Integer, ForeignKey("DIALOGS.id"))
    sender_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer, nullable=False)
    s_l = Column(String(5), nullable=False)
    t_l = Column(String(5), nullable=False)
    text = Column(String(65536), nullable=False)
    translation = Column(String(131072), nullable=True)

    dialog = relationship("Dialog", back_populate="messages")
    sender = relationship("User", back_populate="messages_sent")
    receiver = relationship("User", back_populate="messages_received")


    @classmethod
    def add_message(cls, dialog_id, sender_id, receiver_id, s_l, t_l, text, translation=None, date=datetime.utcnow()):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_message = cls(
            dialog_id=dialog_id,
            sender_id=sender_id,
            receiver_id=receiver_id,
            s_l=s_l,
            t_l=t_l,
            text=text,
            translation=translation,
            date=date
        )
        session.add(new_message)
        session.commit()


Base.metadata.create_all(db.sqlalchemy_engine)