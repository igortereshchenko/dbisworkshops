from sqlalchemy import Column, Integer, Float, String, ForeignKey, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from orm.database_connection import  engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Students(Base):
	__tablename__ = 'students'
	student_id = Column(Integer,primary_key = True)
	student_name  = Column(String(100),nullable=False)
	student_abitur = Column(Boolean,nullable=False)
	student_sex = Column(String(6),nullable=False)
	
	
	recom = relationship('Recom_List',back_populates='student_recom')

class Regions(Base):
	__tablename__ = 'regions'
	region_id = Column(Integer,primary_key=True)
	region_name = Column(String(100),nullable=False)

	recom = relationship('Recom_Base',back_populates='region')
	reg_uni_id = relationship('Reg_Uni', back_populates='region')

class Faculties(Base):
	__tablename__ = 'faculties'
	faculty_id = Column(Integer, primary_key=True)
	faculty_name = Column(Integer, nullable=False)

	# recom = relationship('Recom_Base',back_populates='faculty')

class Univers(Base):
	__tablename__ = 'univers'
	univer_id = Column(Integer,primary_key=True)
	univer_name = Column(String,nullable=False)

	recom = relationship('Recom_Base',back_populates='univer')
	reg_uni_id = relationship('Reg_Uni',back_populates='univer')

class Reg_Uni(Base):
	__tablename__ = 'reg_uni'
	region_id = Column(Integer,ForeignKey('regions.region_id'),primary_key=True)
	univer_id = Column(Integer,ForeignKey('univers.univer_id'),primary_key=True)

	region = relationship('Regions', back_populates='reg_uni_id')
	univer = relationship('Univers', back_populates='reg_uni_id')

class Specialties(Base):
	__tablename__ = 'specialties'
	specialty_id = Column(Integer,primary_key=True)
	specialty_name = Column(String(200),nullable=False)

	recom = relationship('Recom_Base',back_populates='specialty')


class Zno_Scores(Base):
	__tablename__ = 'zno_scores'
	zno_score_id = Column(Integer,primary_key=True)
	zno_score_name = Column(String(100),nullable=False)
	zno_score_value = Column(Float,nullable=False)
	zno_score_student_id = Column(Integer,ForeignKey('students.student_id'),nullable=False)
	
	student_zno = relationship('Students')


class Recom_List(Base):
	__tablename__ = 'recom_list'
	id = Column(Integer, primary_key=True)
	recom_id = Column(Integer, ForeignKey('recom_base.id'))
	recom_student_id = Column(Integer, ForeignKey('students.student_id'),nullable=False)
	recom_crit = Column(Float)
	student_score = Column(Float)
	
	student_recom = relationship('Students',back_populates='recom')
	base_recom = relationship('Recom_Base', back_populates='recom')


class Recom_Base(Base):
	__tablename__ = 'recom_base'
	id = Column(Integer, primary_key=True)
	recom_specialty_id = Column(Integer,ForeignKey('specialties.specialty_id'), nullable=False)
	recom_region_id = Column(Integer, ForeignKey('regions.region_id'),nullable=False)
	recom_univer_id = Column(Integer, ForeignKey('univers.univer_id'),nullable=False)
	recom_faculty_name = Column(String, nullable=False)
	recom_average_score = Column(Float, nullable=False)
	recom_subjects = Column(JSON, nullable=False)


	specialty = relationship('Specialties',back_populates='recom')
	region = relationship('Regions',back_populates='recom')
	univer = relationship('Univers',back_populates='recom')


	recom = relationship('Recom_List', back_populates='base_recom')


Base.metadata.create_all(engine)

