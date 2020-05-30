from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, Date
from sqlalchemy.ext.declarative import declarative_base
from database_connection import engine

Base = declarative_base()

class OrderSong(Base):
    __tablename__ = 'OrderSong'
    song_id = Column(Integer, primary_key=True)
    song_name = Column(String(200))
    song_artist = Column(String(200))

class Broadcast(Base):
    __tablename__ = 'Broadcast'
    broadcast_id = Column(Integer, primary_key=True)
    broadcast_date = Column(Date, nullable=False)
    broadcast_time = Column(String(6), nullable=False)

class Chain(Base):
    __tablename__ = 'Chain'
    broadcast_id_fk = Column(Integer, ForeignKey('Broadcast.broadcast_id'), primary_key=True)
    song_id_fk = Column(Integer, ForeignKey('OrderSong.song_id'), primary_key=True)
    status = Column(Boolean)

class Announcement(Base):
    __tablename__ = 'Announcement'
    announcement_id = Column(Integer, primary_key=True)
    announcement_text = Column(String(2000), nullable=False)

class AnnouncementChain(Base):
    __tablename__ = 'AnnouncementChain'
    broadcast_id_fk = Column(Integer, ForeignKey('Broadcast.broadcast_id'), primary_key=True)
    announcement_id_fk = Column(Integer, ForeignKey('Announcement.announcement_id'), primary_key=True)
    status = Column(Boolean)

class feedback(Base):
    __tablename__ = 'Feedback'
    feedback_id = Column(Integer, primary_key=True)
    feedback_text = Column(String(2000), nullable=False)

class Statistic(Base):
    __tablename__ = 'Statistic'
    statistic_day = Column(String(15), primary_key=True)
    statistic_time = Column(String(6), primary_key=True)
    statistic_count = Column(Integer)


Base.metadata.create_all(engine)
#Base.metadata.drop_all(engine)