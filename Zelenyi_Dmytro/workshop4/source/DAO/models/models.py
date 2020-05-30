from sqlalchemy import Integer, String, Text, Column, MetaData, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType
from Zelenyi_Dmytro.workshop4.source.database_connection import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import re
Base = declarative_base()
meta = MetaData()


class photographers(Base):
    __tablename__ = 'photographers'

    email = Column(String(30), primary_key=True, nullable=False)
    user_password = Column(String(30), nullable=False)
    photographer_name = Column(String(30), nullable=False)
    photographer_surname = Column(String(30))
    gender = Column(String(20), nullable=False)
    about_photographer = Column(Text(), nullable=False)
    birthday = Column(DateTime)
    experience = Column(Integer, nullable=False)
    region = Column(String(30), nullable=False)
    city = Column(String, nullable=False)
    is_premium = Column(String(1))

    CheckConstraint('experience > 0', name='check_experience')


    @classmethod
    def add(cls, email, user_password, photographer_name, photographer_surname, gender, about_photographer,
            birthday, experience, region, city, is_premium):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return -1
        elif not photographer_name.isalpha() or not photographer_surname.isalpha() or not region.isalpha() \
                or not city.isalpha():
            return -1
        elif gender != "Male" or gender != "Famale":
            return -1
        elif is_premium != "N" or is_premium != "Y":
            return -1

        Session = sessionmaker(bind=engine)
        session = Session()

        print("Added")

        photographer = photographers(email=email, user_password=user_password, photographer_name=photographer_name,
                                         photographer_surname=photographer_surname, gender=gender,
                                         about_photographer=about_photographer, birthday=birthday, experience=experience,
                                         region=region, city=city, is_premium=is_premium)

        session.add(photographer)
        session.commit()


class contacts(Base):
    __tablename__ = 'contacts'

    email = Column(String(30), ForeignKey('photographers.email'), primary_key=True, nullable=False)
    phone_number = Column(String(20))
    instagram = Column(String(50))
    facebook = Column(String(50))
    skype = Column(String(50))
    telegram = Column(String(50))

    contact_fk = relationship("photographers", foreign_keys=[email])


    @classmethod
    def add(cls, email, phone_number, instagram, facebook, skype, telegram):
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Added")

        contact = contacts(email=email, phone_number=phone_number, instagram=instagram, facebook=facebook,
                           skype=skype, telegram=telegram)

        session.add(contact)
        session.commit()


class serveces(Base):
    __tablename__ = 'services'

    email = Column(String(30), ForeignKey('photographers.email'), primary_key=True, nullable=False)
    object_shooting = Column(Float)
    portrait_shooting = Column(Float)
    wedding_photo_shoot = Column(Float)
    family_photo_shot = Column(Float)
    event_photography = Column(Float)
    reportage_shooting = Column(Float)
    childrens_photo_shoot = Column(Float)
    interior_shooting = Column(Float)
    photosession_love_story = Column(Float)
    pregnant_photoshoot = Column(Float)
    neither = Column(Float)

    CheckConstraint('object_shooting > 0', name='check_object_shooting')
    CheckConstraint('portrait_shooting > 0', name='check_portrait_shooting')
    CheckConstraint('wedding_photo_shoot > 0', name='check_wedding_photo_shoot')
    CheckConstraint('family_photo_shot > 0', name='check_family_photo_shot')
    CheckConstraint('event_photography > 0', name='check_event_photography')
    CheckConstraint('reportage_shooting > 0', name='check_reportage_shooting')
    CheckConstraint('childrens_photo_shoot > 0', name='check_childrens_photo_shoot')
    CheckConstraint('interior_shooting > 0', name='check_interior_shooting')
    CheckConstraint('photosession_love_story > 0', name='check_photosession_love_story')
    CheckConstraint('pregnant_photoshoot > 0', name='check_pregnant_photoshoot')
    CheckConstraint('neither > 0', name='check_neither')

    serveces_fk = relationship("photographers", foreign_keys=[email])

    @classmethod
    def add(cls, email, object_shooting, portrait_shooting, wedding_photo_shoot, family_photo_shot,
            event_photography, reportage_shooting, childrens_photo_shoot, interior_shooting,
            photosession_love_story, pregnant_photoshoot, neither):
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Added")

        servece = serveces(email=email, object_shooting=object_shooting, portrait_shooting=portrait_shooting,
                           wedding_photo_shoot=wedding_photo_shoot, family_photo_shot=family_photo_shot,
                           event_photography=event_photography, reportage_shooting=reportage_shooting,
                           childrens_photo_shoot=childrens_photo_shoot, interior_shooting=interior_shooting,
                           photosession_love_story=photosession_love_story,pregnant_photoshoot=pregnant_photoshoot,
                           neither=neither)

        session.add(servece)
        session.commit()


class comments(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, primary_key=True)
    email_customer = Column(String(30), ForeignKey('customers.email'), nullable=False)
    email_photographer = Column(String(30), ForeignKey('photographers.email'), nullable=False)
    comment_text = Column(Text(), nullable=False)

    comments_customer_fk = relationship("customers", foreign_keys=[email_customer])
    comments_photographer_fk = relationship("photographers", foreign_keys=[email_photographer])

    @classmethod
    def add(cls, comment_id, email_customer, email_photographer, comment_text):
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Added")

        comment = comments(comment_id=comment_id, email_customer=email_customer, email_photographer=email_photographer,
                           comment_text=comment_text)

        session.add(comment)
        session.commit()


class portfolios(Base):
    __tablename__ = 'portfolios'

    portfolio_id = Column(Integer, primary_key=True)
    author_email = Column(String(30), ForeignKey('photographers.email'), nullable=False)
    img_src = Column(String(50), nullable=False)

    portfolios_fk = relationship("photographers", foreign_keys=[author_email])

    @classmethod
    def add(cls, portfolio_id, author_email, img_src):
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Added")

        portfolio = portfolios(portfolio_id=portfolio_id, author_email=author_email, img_src=img_src)

        session.add(portfolio)
        session.commit()


class customers(Base):
    __tablename__ = 'customers'

    email = Column(String(30), primary_key=True, nullable=False)
    user_password = Column(String(30), nullable=False)
    customer_name = Column(String(30), nullable=False)
    customer_surname = Column(String(30))

    @classmethod
    def add(cls, email, user_password, customer_name, customer_surname):
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Added")

        customer = customers(email=email, user_password=user_password, customer_name=customer_name,
                               customer_surname=customer_surname)

        session.add(customer)
        session.commit()


class history(Base):
    __tablename__ = "history"

    history_id = Column(Integer, primary_key=True)
    customer = Column(String(30), ForeignKey('customers.email'), nullable=False)
    photographer = Column(String(30), ForeignKey('photographers.email'), nullable=False)

    history_customer_fk = relationship("customers", foreign_keys=[customer])
    history_photographer_fk = relationship("photographers", foreign_keys=[photographer])

    @classmethod
    def add(cls, history_id, customer, photographer):
        Session = sessionmaker(bind=engine)
        session = Session()

        print("Added")

        histor = history(history_id=history_id, customer=customer, photographer=photographer)

        session.add(histor)
        session.commit()

Base.metadata.create_all(engine)


# photographers.add("fasfas@gmail.com", "qwerty", "Admin", "Adminov", "Male", "I'm cool", "04-05-1950", 3, "Soup", "Soup", "Y")
