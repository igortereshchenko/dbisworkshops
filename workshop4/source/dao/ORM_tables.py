from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from dao.DB_connection import engine


Base = declarative_base()


class Status(Base):

	__tablename__ = 'status'

	record_id = Column(Integer, primary_key=True)
	gender = Column(String(6), nullable=False)
	education = Column(String(5), nullable=False)
	smoker = Column(String(1), nullable=False)
	sigs_per_day = Column(Integer, nullable=False)
	blood_pressure = Column(String(1), nullable=False)
	prevalent_stroke = Column(String(1), nullable=False)
	prevalent_hyp = Column(String(1), nullable=False)
	diabetes = Column(String(1), nullable=False)

	medical_record = relationship('MediacalRecord', back_populates='status')


class MediacalRecord(Base):

	__tablename__ = 'medical_record'

	record_id = Column(Integer, ForeignKey('status.record_id'), primary_key=True)
	tot_chol = Column(Float, nullable=False)
	sys_bp = Column(Float, nullable=False)
	dia_bp = Column(Float, nullable=False)
	body_index = Column(Float, nullable=False)
	heart_rate = Column(Float, nullable=False)
	glucose = Column(Float, nullable=False)

	status = relationship('Status', back_populates='medical_record')




Base.metadata.create_all(engine)