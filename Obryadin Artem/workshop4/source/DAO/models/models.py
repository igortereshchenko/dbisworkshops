from sqlalchemy import Integer, String, Column, MetaData, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType
from database_connection import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import re
Base = declarative_base()
meta = MetaData()


class game(Base):
    __tablename__ = 'game'
    game_name = Column(String(200), primary_key=True, nullable=False)
    author = Column(String(80), primary_key=True, nullable=False)
    price = Column(Float, primary_key=True, nullable=False)
    genre = Column(String(50), primary_key=True, nullable=False)
    on_storage = Column(Integer, nullable=False)
    game_description = Column(String(500), nullable=False)
    game_edition = Column(String(50), nullable=False)
    number_of_purchases = Column(Integer, nullable=False)
    CheckConstraint('price > 0', name='check_price')
    CheckConstraint('on_storage >= 0', name='check_number_of_purchases')
    CheckConstraint('number_of_purchases >=0', name='check_on_storage')

    @classmethod
    def add(cls, game_name, author, price, genre, on_storage, game_description, game_edition, number_of_purchases):
        if not game_name.isalpha() or not author.isalpha() or not genre.isalpha() or not game_description.isalpha() \
                or not game_edition.isalpha() or not isinstance(price, float) \
                or not isinstance(number_of_purchases, int):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        game = game(game_name=game_name, author=author, price=price, genre=genre, on_storage=on_storage,
                    game_description=game_description, game_edition=game_edition,
                    number_of_purchases=number_of_purchases)
        session.add(game)
        session.commit()

class customer(Base):
    __tablename__ = 'customer'

    first_name = Column(String(100), nullable=False)
    second_name = Column(String(100))
    email = Column(EmailType, primary_key=True, nullable=False)
    user_login = Column(String(40), nullable=False)
    user_password = Column(String(50), nullable=False)

    @classmethod
    def add(cls, first_name, second_name, email, user_login, user_password):
        if not first_name.isalpha() or not second_name.isalpha() or not user_login.isalpha() \
                or not user_password.isalpha() or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        customer1 = customer(first_name=first_name, second_name=second_name, email=email, user_login=user_login,
                    user_password=user_password)
        session.add(customer1)
        session.commit()

class discount(Base):
    __tablename__ = 'discount'

    game_name = Column(String(200), ForeignKey('game.game_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('game.author'), primary_key=True, nullable=False)
    game_price_fk = Column(Float, ForeignKey('game.author'))
    game_genre_fk = Column(String(50), ForeignKey('game.genre'))
    discounts = Column(Integer, nullable=False)
    discount_time = Column(DateTime, nullable=False)
    CheckConstraint('discounts > 0', name='check_discounts')
    CheckConstraint('game_price_fk >= 0', name='check_game_price_fk')
    games = relationship("game", foreign_keys=[game_name])
    games1 = relationship("game", foreign_keys=[author])
    games2 = relationship("game", foreign_keys=[game_price_fk])
    games3 = relationship("game", foreign_keys=[game_genre_fk])

    @classmethod
    def add(cls, game_name, author, game_price_fk, game_genre_fk, discounts, discount_time):
        if not game_name.isalpha() or not author.isalpha() or not game_genre_fk.isalpha() \
                or not isinstance(game_price_fk, float) or not isinstance(discounts, int):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        discount1 = discount(game_name=game_name, author=author, game_price_fk=game_price_fk,
                             game_genre_fk=game_genre_fk, discounts=discounts, discount_time=discount_time)
        session.add(discount1)
        session.commit()


class game_notification(Base):
    __tablename__ = 'game_notification'

    game_name = Column(String(200), ForeignKey('game.game_name'), nullable=False)
    author = Column(String(80), ForeignKey('game.author'), nullable=False)
    game_price_fk = Column(Float, ForeignKey('game.author'))
    game_genre_fk = Column(String(50), ForeignKey('game.genre'))
    notification_text = Column(String(500), nullable=False)
    notification_time = Column(DateTime, primary_key=True, nullable=False)
    games = relationship("game", foreign_keys=[game_name])
    games1 = relationship("game", foreign_keys=[author])
    games2 = relationship("game", foreign_keys=[game_price_fk])
    games3 = relationship("game", foreign_keys=[game_genre_fk])

    @classmethod
    def add(cls, game_name, author, game_price_fk, game_genre_fk, notification_text, notification_time):
        if not game_name.isalpha() or not author.isalpha() or not game_genre_fk.isalpha() \
                or not notification_text.isalpha() or not isinstance(game_price_fk, float):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        game_notification1 = game_notification(game_name=game_name, author=author, game_price_fk=game_price_fk,
                             game_genre_fk=game_genre_fk, notification_text=notification_text,
                             notification_time=notification_time)
        session.add(game_notification1)
        session.commit()


class recomendation(Base):
    __tablename__ = 'recomendation'

    game_name = Column(String(200), ForeignKey('game.game_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('game.author'), primary_key=True, nullable=False)
    price = Column(Float, ForeignKey('game.author'), nullable=False)
    genre = Column(String(50), ForeignKey('game.genre'), nullable=False)
    CheckConstraint('price >= 0', name='check_price')
    games = relationship("game", foreign_keys=[game_name])
    games1 = relationship("game", foreign_keys=[author])
    games2 = relationship("game", foreign_keys=[price])
    games3 = relationship("game", foreign_keys=[genre])

    @classmethod
    def add(cls, game_name, author, price, genre):
        if  not author.isalpha() or not genre.isalpha() or not isinstance(price, float):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        recomendation1 = recomendation(game_name=game_name, author=author, price=price, genre=genre)
        session.add(recomendation1)
        session.commit()

class review(Base):
    __tablename__ = 'review'
    game_name = Column(String(200), ForeignKey('game.game_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('game.author'), primary_key=True, nullable=False)
    game_price_fk = Column(Float, ForeignKey('game.author'))
    game_genre_fk = Column(String(50), ForeignKey('game.genre'))
    game_mark = Column(Integer, nullable=False)
    reviews = Column(String(500), nullable=False)
    rating = Column(Integer, nullable=False)
    CheckConstraint('game_price_fk >= 0', name='check_game_price_fk')
    CheckConstraint('game_mark >= 0', name='check_game_mark')
    CheckConstraint('rating >= 0', name='check_rating')
    games = relationship("game", foreign_keys=[game_name])
    games1 = relationship("game", foreign_keys=[author])
    games2 = relationship("game", foreign_keys=[game_price_fk])
    games3 = relationship("game", foreign_keys=[game_genre_fk])

    @classmethod
    def add(cls, game_name, author, game_price_fk, game_genre_fk, game_mark, reviews, rating):
        if  not author.isalpha() or not game_genre_fk.isalpha() \
                or not isinstance(game_price_fk, float) or not reviews.isalpha() \
                or not isinstance(game_mark, int) or not isinstance(rating, int):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        review1 = review(game_name=game_name, author=author, game_price_fk=game_price_fk,
                         game_genre_fk=game_genre_fk, game_mark=game_mark, reviews=reviews, rating=rating)
        session.add(review1)
        session.commit()


class desired(Base):
    __tablename__ = 'desired'
    game_name = Column(String(200), ForeignKey('game.game_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('game.author'), primary_key=True, nullable=False)
    price = Column(Float, ForeignKey('game.author'), nullable=False)
    genre = Column(String(50), ForeignKey('game.genre'), nullable=False)
    CheckConstraint('price >= 0', name='check_price')
    games = relationship("game", foreign_keys=[game_name])
    games1 = relationship("game", foreign_keys=[author])
    games2 = relationship("game", foreign_keys=[price])
    games3 = relationship("game", foreign_keys=[genre])

    @classmethod
    def add(cls, game_name, author, price, genre):
        if not author.isalpha() or not genre.isalpha() or not isinstance(price, float):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        desired1 = desired(game_name=game_name, author=author, price=price,
                         genre=genre)
        session.add(desired1)
        session.commit()


class game_order(Base):
    __tablename__ = 'game_order'

    game_name = Column(String(200), ForeignKey('game.game_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('game.author'), primary_key=True, nullable=False)
    price = Column(Float, ForeignKey('game.author'))
    game_genre_fk = Column(String(50), ForeignKey('game.genre'), nullable=False)
    status = Column(String(50), nullable=False)
    CheckConstraint('price >= 0', name='check_price')
    games = relationship("game", foreign_keys=[game_name])
    games1 = relationship("game", foreign_keys=[author])
    games2 = relationship("game", foreign_keys=[price])
    games3 = relationship("game", foreign_keys=[game_genre_fk])

    @classmethod
    def add(cls, game_name, author, price, game_genre_fk, status):
        if not author.isalpha() or not game_genre_fk.isalpha() \
                or not isinstance(price, float) or not status.isalpha():
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        game_order1 = game_order(game_name=game_name, author=author, price=price, game_genre_fk=game_genre_fk,
                                 status=status)
        session.add(game_order1)
        session.commit()


Base.metadata.create_all(engine)

# game.add('asa', 'bsa', 2, 'asa', 2, 'asd', 'qwq', 5)
# customer.add('as', 'bs', "qweq@gmail.com", 'as', "as")
# discount.add('as', 'bs', 2, "as", 12, "01-02-2000")
# game_notification.add('as', 'bs', 2, "as", "asd", "01-02-2000")
# recomendation.add('as', 'bs', 2, "as")
# review.add('as', 'bs', 2, 'as', 1, 'asdas', 2)
# desired.add('as', 'bs', 2, 'as')
# game_order.add('as', 'bs', 2, 'as', 'asa')