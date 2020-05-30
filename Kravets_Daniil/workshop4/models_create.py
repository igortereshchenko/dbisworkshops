from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Time, Date
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine

Base = declarative_base()

class OrderSong(Base):
    __tablename__ = 'OrderSong'
    song_id = Column(Integer, primary_key=True)
    song_name = Column(String(50), nullable=False)
    song_artist = Column(String(50), nullable=False)
    status = Column(Boolean)

class Broadcast(Base):
    __tablename__ = 'Broadcast'
    broadcast_id = Column(Integer, primary_key=True)
    broadcast_date = Column(DateTime, nullable=False, unique=True)

class Chain(Base):
    __tablename__ = 'Chain'
    broadcast_id_fk = Column(Integer, ForeignKey('Broadcast.broadcast_id'), primary_key=True)
    song_id = Column(Integer, ForeignKey('OrderSong.song_id'), primary_key=True)
    status = Column(Boolean)

class Announcement(Base):
    __tablename__ = 'Announcement'
    announcement_id = Column(Integer, primary_key=True)
    announcement_text = Column(String(1000), nullable=False)

class AnnouncementChain(Base):
    __tablename__ = 'AnnouncementChain'
    broadcast_id_fk = Column(Integer, ForeignKey('Broadcast.broadcast_id'), primary_key=True)
    announcement_id_fk = Column(Integer, ForeignKey('Announcement.announcement_id'), primary_key=True)
    status = Column(Boolean)

class feedback(Base):
    __tablename__ = 'feedback'
    feedback_id = Column(Integer, primary_key=True)
    feedback_date = Column(DateTime, nullable=False)
    feedback_text = Column(String(1000), nullable=False)

class help(Base):
    __tablename__ = 'help'
    help_id = Column(Integer, primary_key=True)
    help_info = Column(String(1000), nullable=False)

Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)