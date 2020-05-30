from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
import connection
from connection import engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin


Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()



class DOCTOR(Base):
    __tablename__ = "DOCTOR"
    id = Column(Integer, primary_key=True)
    username= Column(String(20))
    name = Column(String(20))
    surname = Column(String(20))
    password = Column(String(20))
    hospital = Column(Integer)
    doc_card = relationship("CARD", backref="parents")
    doc_pac = Column(Integer, ForeignKey('PAC.hospital'))
    UniqueConstraint('username')


    @classmethod
    def RG_DOCTOR(cls, id_user_doctor, username_doctor, pass_user_doctor):
        try:
            if (session.query(DOCTOR).filter_by(id=id_user_doctor).first()).action != 1:
                update = session.query(DOCTOR).filter_by(id=id_user_doctor).first()
                update.action = 1
                session.merge(update)
                row = DOCTOR(username=username_doctor, id=id_user_doctor, password=pass_user_doctor)
                session.add(row)
                search_query = (session.query(DOCTOR).filter_by(id=id_user_doctor).one()).name
                print('Вітаємо лікар,', search_query)
            else:
                print('Такий користувач вже існує')
        except:
            print('Виникла проблема')


    @classmethod
    def LG_DOCTOR(cls, id_doctor, username_doctor, pass_doctor):
        try:
            check = session.query(DOCTOR).filter_by(username=username_doctor, password=pass_doctor).all()
            for i in check:
                id = i.id
            get_name = session.query(DOCTOR).filter_by(id=id_doctor).all()
            for i in get_name:
                print('Вітаємо лікар,', i.name)
        except:
            print('Виникла проблема')


class PAC(Base):
    __tablename__ = "PAC"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    surname = Column(String(20))
    username = Column(String(20))
    hospital= Column(String(20))
    password = Column(String(20))
    pac_card = relationship("CARD", backref="parents")
    doc_pac = relationship("DOCTOR", backref="parents")
    UniqueConstraint('username')


    @classmethod
    def RG_PAC(cls, id_pac, username_pac, pass_pac):
        try:
            if (session.query(PAC).filter_by(id=id_pac).first()).action != 1:
                update = session.query(PAC).filter_by(id=id_pac).first()
                update.action = 1
                session.merge(update)
                row = PAC(username=username_pac, id=id_pac, password=pass_pac)
                session.add(row)
                search_query = (session.query(PAC).filter_by(id=id_pac).one()).name
                print('Вітаємо пацієент,', search_query)
            else:
                print('Такий користувач вже існує')
        except:
            print('Виникла проблема')


    @classmethod
    def LG_PAC(cls, id_pac, username_pac, pass_pac):
        try:
            check = session.query(PAC).filter_by(username=username_pac, password=pass_pac).all()
            for i in check:
                id = i.id_pac
            get_name = session.query(PAC).filter_by(id=id_pac).all()
            for i in get_name:
                print('Вітаємо пацієнт,', i.name)
        except:
            print('Виникла проблема')

    @classmethod
    def search(cls, id, username):
        try:
            if id != None and username != None:
                search_query = session.query(PAC).filter_by(id=id, username=username).all()
            elif id != None:
                search_query = session.query(PAC).filter_by(id=id).all()
            elif username != None:
                search_query = session.query(PAC).filter_by(username=username).all()
            for row in search_query:
                print(row.id, row.username)
        except:
            print("Не знайдено!")


class CARD(Base):
    __tablename__ = "CARD"
    id = Column(Integer, primary_key=True)
    username=Column(String(20))
    hospital = Column(Integer)
    hirurg = Column(String(20))
    lor = Column(String(20))
    cardiolog = Column(String(20))
    privivki = Column(String(20))
    pac_card = Column(Integer, ForeignKey('PAC.hospital'))
    doc_card = Column(Integer, ForeignKey('DOCTOR.hospital'))
    diag_card = relationship("DIAGNOS", backref="parents")
    UniqueConstraint('username')

    def new_card():
        form = PatientForm()
        error = None
        username = list(db.sqlalchemy_session.query(CARD.username))
        users = []
        for i in range(len(username)):
            users.append(username[i][0])
        if request.method == 'POST':
            if not form.validate():
                return "Додати"
            else:
                patient_id = list(db.sqlalchemy_session.query(func.max(patient.id)))[0][0]
                if form.username.data in users:
                    return '//'
                else:
                    patient_obj = CARD(
                        id= id + 1,
                        username=form.username.data,
                        hirurg=form.hirurg.data,
                        lor=form.lor.data,
                        cardiolog=form.cardiolog.data,
                        privivki=form.cardiolog.data
                    )
                    db.sqlalchemy_session.add(patient_obj)
                    db.sqlalchemy_session.commit()
                    return 'Виконано'
        return '//'



    @classmethod
    def add(cls, id, hirurg, lor, cardiolog, privivki):
        if not id.isalpha():
            print("Не існує такої картки!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        card = CARD(id=id, hirurg=hirurg, lor=lor, cardiolog=cardiolog, privivki=privivki)
        session.add(card)
        session.commit()


class DIAGNOS(Base):
    __tablename__ = 'DIAGNOS'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    info = Column(String(100))
    diag_card = Column(Integer, ForeignKey('CARD.id'))



    @classmethod
    def prov(cls, id, info):
        if not all(x.isalpha()or x.isspace() for x in name) or not (x.isalpha()or x.isspace() for x in info):
            print('Неправильно введні данні!!!')
            return -1
        prov = Prov(id = id, info=info)
        session.add(prov)
        session.commit()

    @classmethod
    def ins(cls,id_pac, info):
        idnotes = session.query(DIAGNOS).filter(DIAGNOS.id== id_pac)
        id_notes = [row.id for row in idnotes]
        if (len(id_notes) < 100):
            new_note = DIAGNOS(id=id_pac, info=info)
            session.add(new_note)
            session.commit()
        else:
            print("Перевищує допустиму кількість знаків")

Base.metadata.create_all(engine)
