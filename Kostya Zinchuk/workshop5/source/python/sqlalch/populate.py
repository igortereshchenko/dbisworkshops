from datetime import date
from sqlalch.forms import Book, User, UserBook
from sqlalch.db_conn import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
new_book = Book.add_book(1, "For whom the Bell Tolls", "Ernest",
"Hemingway",
"https://briefly.ru/heminguej/po_kom_zvonit_kolokol/")

session.commit()