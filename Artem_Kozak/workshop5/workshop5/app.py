from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# for local run
# os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'
# os.environ['DATABASE_URL'] = 'postgresql://workshops:root@localhost/workshops_db'

# for HEROKU
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Book


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add')
def add_book():
    name = request.args.get('name')
    author = request.args.get('author')
    publisher = request.args.get('publisher')

    try:
        book = Book(name, author, publisher)

        db.session.add(book)
        db.session.commit()

        return 'book added {}'.format(book.id)

    except Exception as error:
        return str(error)


@app.route('/all')
def get_all():
    try:
        books = Book.query.all()

        return jsonify([book.serialize() for book in books])

    except Exception as error:
        return str(error)


@app.route('/get/<book_id>')
def get_by_id(book_id):
    try:
        book = Book.query.filter_by(id=book_id).first()
        return jsonify(book)

    except Exception as error:
        return str(error)


if __name__ == '__main__':
    app.run()
