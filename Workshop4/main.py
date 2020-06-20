import uuid
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column,  Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

engine = create_engine(
    oracle_connection_string.format(

        username="OUTLN",
        password="1234",
        sid="orcl",
        host="localhost",
        port="1521",
        database="orcl",

    )
    , echo=True
)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session(autocommit=True,autoflush=True)


class Insurer(Base):
    __tablename__ = 'insurer_log'

    id = Column(String(100), primary_key=True)
    insurer_name = Column(String(50))
    insurer_password = Column(Integer)
    insurer_email = Column(String(50))
    styles = relationship('Personalinfo', backref = backref('insurer_log'), lazy=True)


    def __init__(self,  insurer_name, insurer_password, insurer_email):
        self.insurer_name = insurer_name
        self.insurer_password = insurer_password
        self.insurer_email = insurer_email
        self.id = str(uuid.uuid4())

    def get_id(self):
        return self.id



class Personalinfo(Base):
        __tablename__ = 'personal_info'

        id = Column(String(100), primary_key=True)
        id_person = Column(String(100), ForeignKey("insurer_log.id"))
        person_firststname = Column(String(50))
        person_lastname = Column(String(50))
        person_age = Column(Integer)
        person_passport = Column(Integer)
        person_itin = Column(Integer)
        person_cityzenship = Column(String(50))

        def __init__(self, person_firststname, person_lastname, person_age, person_passport, person_itin, person_cityzenship):
            self.id = str(uuid.uuid4())
            self.id_person = Insurer.get_id()
            self.person_firststname = person_firststname
            self.person_lastname = person_lastname
            self.person_age= person_age
            self.person_passport = person_passport
            self.person_itin = person_itin
            self.person_cityzenship = person_cityzenship

        def check_age_value(id, age, values, person_id):
            if age > 70 and age < 1:
                print('Unacceptable age')
            else:
                row = Personalinfo(id=id, person_age=values, id_person=person_id)
                session.add(row)
                session.commit()

        def check_cityzenship(id, country, values, person_id):
            if country != 'Ukraine':
                print('only for citizens of Ukraine ')
            else:
                l = Personalinfo(id=id, person_cityzenship=values, id_person=person_id)
                session.add(l)
                session.commit()





class Policy(Base):
    __tablename__ = 'policy_type'

    id = Column(String(100), ForeignKey('insurer_log.id'), primary_key=True)
    policy = Column(String(50), default="basic", primary_key=True)
    policies = ['basic', 'business', 'sport', 'active']

    def __init__(self, Insurer):
        self.id = Insurer.get_id()

    def add_policy(self, policy):
        if policy in self.policies:
            self.policy = policy

    def check_policy(self, Insurer, policy):
        policies = session.query(Policy).filter_by(id=Insurer.get_id()).all()
        return any(i.policy == policy for i in policies)



Base.metadata.create_all(engine)


a = Insurer("Liza", 123, "liza@gmail.com")
session.add(a)
session.flush()

#b = Personalinfo(person_firststname='Elizabeth', person_lastname='Komarova', person_age = 19, person_passport = 234467, person_itin = 3334444, person_cityzenship = 'Ukraine', insurer_log=a)
#session.add(b)
#session.flush()

#session.add(Policy(b.get_id(), ['basic']))
#.commit()
#session.flush()
#session.close()
