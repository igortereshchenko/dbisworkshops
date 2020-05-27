from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from oracledb import *

Base = declarative_base()
db = OracleDb()

class Vendors(Base):

    __tablename__ = 'Ivents'
    id = Column(Integer, primary_key=True)
    vendor_name = Column(String, unique=True)
    vendor_email = Column(String, nullable=False)
    ticket_number = Column(Integer, nullable = False)
    
    @classmethod
    def add_vendor(self,u_vendor_name, u_vendor_email, u_ticket_number):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_vendor = Vendors(
                vendor_name=u_vendor_name,
                vendor_email=u_vendor_email,
                ticket_number = id_ticket_number
                )
        session.add(new_vendor)
        session.commit()

class Ivents(Base):

    __tablename__ = 'Ivents'
    id = Column(Integer, primary_key=True)
    event_name = Column(String, unique=True)
    event_category = Column(String, nullable=False)
    event_date = Column(DateTime, nullable=False)
    vendor_id = relationship("Vendors", backref="Ivents" )
    ticket_number = relationship("Vendors", backref="Ivents" )
    
    @classmethod
    def add_ivents(self,u_event_name, u_event_category, u_event_date, u_vendor_id, u_ticket_number):
        db = OracleDb()
        session = db.sqlalchemy_session
        idvendor = session.query(Vendors).filter(Vendors.id == u_vendor_id)
        id_vendor = [row.vendor_id for row in idvendor][0]
        numberticket = session.query(Vendors).filter(Vendors.ticket_number == u_ticket_number)
        number_ticket = [row.ticket_number for row in numberticket][0]
        new_ivent = Ivents(
                event_name=u_event_name
                event_category=u_event_category
                event_date=u_event_date
                vendor_id=id_vendor
                ticket_number=number_ticket
                )
        session.add(new_ivent)
        session.commit()
    
Base.metadata.create_all(db.sqlalchemy_engine)