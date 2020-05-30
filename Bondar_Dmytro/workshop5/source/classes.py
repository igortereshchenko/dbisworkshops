from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from oracledb import *

Base = declarative_base()
db = OracleDb()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)

    @classmethod
    def add_user(self,u_name,u_username, u_password):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_user = User(
                name=u_name,
                username=u_username,
                password=u_password
                )
        session.add(new_user)
        session.commit()
        new_user.get_id(u_username)
        
    @classmethod
    def get_id(self,u_username):
        db = OracleDb()
        q = db.execute("select id from users where username='{0}'".format(u_username))
        self.id = q[0][0]
        
        
        
class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    event_date = Column(Date)
    start_id = Column(Integer, ForeignKey("time_dim.id"))
    end_id = Column(Integer, ForeignKey("time_dim.id"))
    repeatedly_id = Column(Integer, ForeignKey("Repeatedly.id"))

    @classmethod
    def add_event(self, u_id, e_name, e_date, s_time, e_time, mon='0', tue='0', wed='0', thu='0', fri='0', sat='0', sun='0' ):
        db = OracleDb()
        db.cursor.callproc("add_event", [u_id, e_name, e_date, s_time, e_time, mon, tue, wed, thu, fri, sat, sun])
        db.connection.commit


    @classmethod
    def event_list(self, u_id, e_date = 0):
        db = OracleDb()
        q = db.execute("select * from list_events where user_id = '{0}'".format(u_id))
        return q


    @classmethod
    def event_plot(self, u_id):
        db = OracleDb()
        q = db.execute("select event_date, count(*) \
                       from list_events \
                       where user_id = '{0}' \
                       group by event_date".format(u_id))
        return q   
    
    
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    @classmethod
    def add_group(self,u_id, g_name):
        db = OracleDb()
        db.cursor.callproc("add_group", [u_id, g_name])
        db.connection.commit
              

class user_event(Base):
    __tablename__ = 'user_event'
    user_id = Column(Integer, ForeignKey("User.id"), primary_key=True)
    event_id  = Column(Integer, ForeignKey("Event.id"), primary_key=True)


class user_group(Base):
    __tablename__ = 'user_group'
    user_id = Column(Integer, ForeignKey("User.id"), primary_key=True)
    group_id  = Column(Integer,ForeignKey("Group.id"), primary_key=True)
    is_admin  = Column(String)
    

class Repeatedly(Base):
    __tablename__ = 'repeatedly'
    id = Column(Integer, primary_key=True)
    monday = Column(String)
    tuesday = Column(String)
    wednesday = Column(String)
    thursday = Column(String)
    friday = Column(String)
    saturday = Column(String)
    sunday = Column(String)
    
    
class time_dim(Base):
    __tablename__ = 'time_dim'
    id = Column(Integer, primary_key=True)
    time  = Column(String)
    hour  = Column(Integer)
    minutes  = Column(Integer)
