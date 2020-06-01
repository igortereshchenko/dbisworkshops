from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dao.connection import engine

Base = declarative_base()


class Doctor(Base):
    __tablename__ = 'doctor'

    doc_id = Column(Integer, primary_key=True)
    doc_name = Column(String(50), nullable=False)
    doc_special = Column(String(50), nullable=False)
    hosp_name = Column(String(50), ForeignKey('hospital.hosp_name'))
    cabinet = Column(Integer, CheckConstraint('pat_age >= 0'), nullable=False)

    #hospital = relationship('Hospital', back_populates='doctor')
    #timetable = relationship('Timetable', back_populates='doctor')


class Hospital(Base):
    __tablename__ = 'hospital'

    hosp_name = Column(String(50), primary_key=True)
    hosp_address = Column(String(50), nullable=False)
    hosp_dist = Column(String(50), nullable=False)

    #doctor = relationship('Doctor', back_populates='hospital')
    #timetable = relationship('Timetable', back_populates='hospital')


class Timetable(Base):
    __tablename__ = 'timetable'

    doc_id = Column(Integer, ForeignKey('doctor.doc_id'), nullable=False)
    hosp_name = Column(String(50), ForeignKey('hospital.hosp_name'), nullable=False)
    pat_name = Column(String(50), nullable=False)
    pat_age = Column(Integer, CheckConstraint('pat_age >= 18'), nullable=False)
    pat_street = Column(String(50), nullable=False)
    pat_dist = Column(String(50), nullable=False)
    time_date = Column(String(50), primary_key=True)


    def __init__(self, doc_id, hosp_name, pat_name, pat_age, pat_street, pat_dist, time_date):
        """"""
        self.doc_id = doc_id
        self.hosp_name = hosp_name
        self.pat_name = pat_name
        self.pat_age = pat_age
        self.pat_street = pat_street
        self.pat_dist = pat_dist
        self.time_date = time_date

    #doctor = relationship('Doctor', back_populates='timetable')
    #hospital = relationship('Hospital', back_populates='timetable')


Base.metadata.create_all(engine)
