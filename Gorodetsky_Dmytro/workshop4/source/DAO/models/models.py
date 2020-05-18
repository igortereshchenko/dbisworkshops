from sqlalchemy import Integer, String, Column, MetaData, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType
from database_connection import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import re
Base = declarative_base()
meta = MetaData()


class book(Base):
    __tablename__ = 'book'
    book_name = Column(String(200), primary_key=True, nullable=False)
    author = Column(String(80), primary_key=True, nullable=False)
    price = Column(Float, primary_key=True, nullable=False)
    genre = Column(String(50), primary_key=True, nullable=False)
    on_storage = Column(Integer, nullable=False)
    book_description = Column(String(500), nullable=False)
    book_edition = Column(String(50), nullable=False)
    number_of_purchases = Column(Integer, nullable=False)
    CheckConstraint('price > 0', name='check_price')
    CheckConstraint('on_storage >= 0', name='check_number_of_purchases')
    CheckConstraint('number_of_purchases >=0', name='check_on_storage')

    @classmethod
    def add(cls, book_name, author, price, genre, on_storage, book_description, book_edition, number_of_purchases):
        if not book_name.isalpha() or not author.isalpha() or not genre.isalpha() or not book_description.isalpha() \
                or not book_edition.isalpha() or not isinstance(price, float) \
                or not isinstance(number_of_purchases, int):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        Book = book(book_name=book_name, author=author, price=price, genre=genre, on_storage=on_storage,
                    book_description=book_description, book_edition=book_edition,
                    number_of_purchases=number_of_purchases)
        session.add(Book)
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

    book_name = Column(String(200), ForeignKey('book.book_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('book.author'), primary_key=True, nullable=False)
    book_price_fk = Column(Float, ForeignKey('book.author'))
    book_genre_fk = Column(String(50), ForeignKey('book.genre'))
    discounts = Column(Integer, nullable=False)
    discount_time = Column(DateTime, nullable=False)
    CheckConstraint('discounts > 0', name='check_discounts')
    CheckConstraint('book_price_fk >= 0', name='check_book_price_fk')
    books = relationship("book", foreign_keys=[book_name])
    books1 = relationship("book", foreign_keys=[author])
    books2 = relationship("book", foreign_keys=[book_price_fk])
    books3 = relationship("book", foreign_keys=[book_genre_fk])

    @classmethod
    def add(cls, book_name, author, book_price_fk, book_genre_fk, discounts, discount_time):
        if not book_name.isalpha() or not author.isalpha() or not book_genre_fk.isalpha() \
                or not isinstance(book_price_fk, float) or not isinstance(discounts, int):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        discount1 = discount(book_name=book_name, author=author, book_price_fk=book_price_fk,
                             book_genre_fk=book_genre_fk, discounts=discounts, discount_time=discount_time)
        session.add(discount1)
        session.commit()


class book_notification(Base):
    __tablename__ = 'book_notification'

    book_name = Column(String(200), ForeignKey('book.book_name'), nullable=False)
    author = Column(String(80), ForeignKey('book.author'), nullable=False)
    book_price_fk = Column(Float, ForeignKey('book.author'))
    book_genre_fk = Column(String(50), ForeignKey('book.genre'))
    notification_text = Column(String(500), nullable=False)
    notification_time = Column(DateTime, primary_key=True, nullable=False)
    books = relationship("book", foreign_keys=[book_name])
    books1 = relationship("book", foreign_keys=[author])
    books2 = relationship("book", foreign_keys=[book_price_fk])
    books3 = relationship("book", foreign_keys=[book_genre_fk])

    @classmethod
    def add(cls, book_name, author, book_price_fk, book_genre_fk, notification_text, notification_time):
        if not book_name.isalpha() or not author.isalpha() or not book_genre_fk.isalpha() \
                or not notification_text.isalpha() or not isinstance(book_price_fk, float):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        book_notification1 = book_notification(book_name=book_name, author=author, book_price_fk=book_price_fk,
                             book_genre_fk=book_genre_fk, notification_text=notification_text,
                             notification_time=notification_time)
        session.add(book_notification1)
        session.commit()


class recomendation(Base):
    __tablename__ = 'recomendation'

    book_name = Column(String(200), ForeignKey('book.book_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('book.author'), primary_key=True, nullable=False)
    price = Column(Float, ForeignKey('book.author'), nullable=False)
    genre = Column(String(50), ForeignKey('book.genre'), nullable=False)
    CheckConstraint('price >= 0', name='check_price')
    books = relationship("book", foreign_keys=[book_name])
    books1 = relationship("book", foreign_keys=[author])
    books2 = relationship("book", foreign_keys=[price])
    books3 = relationship("book", foreign_keys=[genre])

    @classmethod
    def add(cls, book_name, author, price, genre):
        if  not author.isalpha() or not genre.isalpha() or not isinstance(price, float):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        recomendation1 = recomendation(book_name=book_name, author=author, price=price, genre=genre)
        session.add(recomendation1)
        session.commit()

class review(Base):
    __tablename__ = 'review'
    book_name = Column(String(200), ForeignKey('book.book_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('book.author'), primary_key=True, nullable=False)
    book_price_fk = Column(Float, ForeignKey('book.author'))
    book_genre_fk = Column(String(50), ForeignKey('book.genre'))
    book_mark = Column(Integer, nullable=False)
    reviews = Column(String(500), nullable=False)
    rating = Column(Integer, nullable=False)
    CheckConstraint('book_price_fk >= 0', name='check_book_price_fk')
    CheckConstraint('book_mark >= 0', name='check_book_mark')
    CheckConstraint('rating >= 0', name='check_rating')
    books = relationship("book", foreign_keys=[book_name])
    books1 = relationship("book", foreign_keys=[author])
    books2 = relationship("book", foreign_keys=[book_price_fk])
    books3 = relationship("book", foreign_keys=[book_genre_fk])

    @classmethod
    def add(cls, book_name, author, book_price_fk, book_genre_fk, book_mark, reviews, rating):
        if  not author.isalpha() or not book_genre_fk.isalpha() \
                or not isinstance(book_price_fk, float) or not reviews.isalpha() \
                or not isinstance(book_mark, int) or not isinstance(rating, int):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        review1 = review(book_name=book_name, author=author, book_price_fk=book_price_fk,
                         book_genre_fk=book_genre_fk, book_mark=book_mark, reviews=reviews, rating=rating)
        session.add(review1)
        session.commit()


class desired(Base):
    __tablename__ = 'desired'
    book_name = Column(String(200), ForeignKey('book.book_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('book.author'), primary_key=True, nullable=False)
    price = Column(Float, ForeignKey('book.author'), nullable=False)
    genre = Column(String(50), ForeignKey('book.genre'), nullable=False)
    CheckConstraint('price >= 0', name='check_price')
    books = relationship("book", foreign_keys=[book_name])
    books1 = relationship("book", foreign_keys=[author])
    books2 = relationship("book", foreign_keys=[price])
    books3 = relationship("book", foreign_keys=[genre])

    @classmethod
    def add(cls, book_name, author, price, genre):
        if not author.isalpha() or not genre.isalpha() or not isinstance(price, float):
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        desired1 = desired(book_name=book_name, author=author, price=price,
                         genre=genre)
        session.add(desired1)
        session.commit()


class book_order(Base):
    __tablename__ = 'book_order'

    book_name = Column(String(200), ForeignKey('book.book_name'), primary_key=True, nullable=False)
    author = Column(String(80), ForeignKey('book.author'), primary_key=True, nullable=False)
    price = Column(Float, ForeignKey('book.author'))
    book_genre_fk = Column(String(50), ForeignKey('book.genre'), nullable=False)
    status = Column(String(50), nullable=False)
    CheckConstraint('price >= 0', name='check_price')
    books = relationship("book", foreign_keys=[book_name])
    books1 = relationship("book", foreign_keys=[author])
    books2 = relationship("book", foreign_keys=[price])
    books3 = relationship("book", foreign_keys=[book_genre_fk])

    @classmethod
    def add(cls, book_name, author, price, book_genre_fk, status):
        if not author.isalpha() or not book_genre_fk.isalpha() \
                or not isinstance(price, float) or not status.isalpha():
            print("Data is not correct!")
            return -1
        Session = sessionmaker(bind=engine)
        session = Session()
        book_order1 = book_order(book_name=book_name, author=author, price=price, book_genre_fk=book_genre_fk,
                                 status=status)
        session.add(book_order1)
        session.commit()


Base.metadata.create_all(engine)

# book.add('asa', 'bsa', 2, 'asa', 2, 'asd', 'qwq', 5)
# customer.add('as', 'bs', "qweq@gmail.com", 'as', "as")
# discount.add('as', 'bs', 2, "as", 12, "01-02-2000")
# book_notification.add('as', 'bs', 2, "as", "asd", "01-02-2000")
# recomendation.add('as', 'bs', 2, "as")
# review.add('as', 'bs', 2, 'as', 1, 'asdas', 2)
# desired.add('as', 'bs', 2, 'as')
# book_order.add('as', 'bs', 2, 'as', 'asa')