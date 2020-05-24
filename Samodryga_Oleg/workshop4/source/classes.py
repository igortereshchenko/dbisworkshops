from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, insert, select, and_
from sqlalchemy.orm import relationship
from oracledb import *

Base = declarative_base()
db = OracleDb()

class Users(Base):

    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('Country.id'))
    user = relationship("Note", back_populates="Users")
    
    @classmethod
    def add_user(self,u_username, u_password, u_country_name):
        db = OracleDb()
        session = db.sqlalchemy_session
        idcountry = session.query(Country).filter(Country.name == u_country_name)
        id_country = [row.country_id for row in idcountry][0]
        new_user = Users(
                username=u_username,
                password=u_password,
                country_id = id_country
                )
        session.add(new_user)
        session.commit()

class Country(Base):

    __tablename__ = 'Country'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user = relationship("Users", back_populates="Country")
    numbersAid = relationship("NumbersAid", back_populates="Country")
    hospital = relationship("Hospital", back_populates="Country")
    
    @classmethod
    def add_country(self,u_name):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_country = Country(
                name=u_name
                )
        session.add(new_country)
        session.commit()

class NumbersAid(Base):

    __tablename__ = 'NumbersAid'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('Country.id'))
    
    @classmethod
    def add_aidNumber(self, u_phone_number, u_country_name):
        db = OracleDb()
        session = db.sqlalchemy_session
        idcountry = session.query(Country).filter(Country.name == u_country_name)
        id_country = [row.country_id for row in idcountry][0]
        new_aidNumber = NumbersAid(
                phone_number = u_phone_number,
                country_id = id_country
                )
        session.add(new_aidNumber)
        session.commit()

class Hospital(Base):

    __tablename__ = 'Hospital'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    adres = Column(String, nullable=False)
    country_id = Column(Integer, ForeignKey('Country.id'))
    
    @classmethod
    def add_hospital(self, u_name, u_adres, u_country):
        db = OracleDb()
        session = db.sqlalchemy_session
        idcountry = session.query(Country).filter(Country.name == u_country)
        id_country = [row.country_id for row in idcountry][0]
        new_hospital = Hospital(
                name = u_name,
                adres = u_adres,
                country_id = id_country
                )
        session.add(new_hospital)
        session.commit()
    
class Symptom(Base):

    __tablename__ = 'Symptom'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    
    @classmethod
    def add_symptom(self, u_name, u_Description):
        db = OracleDb()
        session = db.sqlalchemy_session
        new_symptom = Symptom(
                name = u_name,
                Description = u_Description
                )
        session.add(new_symptom)
        session.commit()
    
class Note(Base):

    __tablename__ = 'Note'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.id'))
    
    @classmethod
    def add_note(self, u_name, u_Description, id_user):
        db = OracleDb()
        session = db.sqlalchemy_session
        idnotes = session.query(Note).filter(Note.user_id == id_user)
        id_notes = [row.user_id for row in idnotes]
        if(len(id_notes)<41):
            new_note = Note(
                    name = u_name,
                    Description = u_Description,
                    user_id = id_user
                    )
            session.add(new_note)
            session.commit()
        else:
            print("Total notes will be less 40")
    
Base.metadata.create_all(db.sqlalchemy_engine)