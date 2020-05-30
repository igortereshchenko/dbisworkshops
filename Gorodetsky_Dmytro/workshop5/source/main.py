from flask import Flask, request, render_template, url_for, redirect, flash
from forms import RegisterForm, LoginForm, BookForm
from models import Book, Customer, engine, Cart
from sqlalchemy.orm import sessionmaker
import plotly
import plotly.graph_objs as go
import pandas as pd
import json


user_logged = False
user_name = "Not Logged"
first_name = "Not Logged"
second_name = "Not Logged"
current_page = "main_page"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'AAAAAAAA'


def create_plot():
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Book).all()
    session.close()
    names = []
    prices = []
    for i in query:
        names.append(i.book_name)
        prices.append(i.price)
    water_df = pd.DataFrame({'x': names, 'y': prices})
    data = [
        go.Bar(
            x=water_df['x'],
            y=water_df['y'],
            name='Price of books'
        )
    ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def create_pie():
    Session = sessionmaker(bind=engine)
    session = Session()
    a = session.query(Book).filter(Book.genre == 'Fantasy').all()
    b = session.query(Book).filter(Book.genre == 'Horror').all()
    c = session.query(Book).filter(Book.genre == 'Scince').all()
    session.close()

    fantasy = 0
    horror = 0
    scince = 0
    for i in a:
        fantasy += i.number_of_purchases

    for i in b:
        horror += i.number_of_purchases

    for i in c:
        scince += i.number_of_purchases

    graph_values = [{
        'labels': ["Fantasy", "Horror", "Science"],
        'values': [fantasy, horror, scince],
        'type': 'pie',
        'insidetextfont': {'color': '#FFFFFF',
                           'size': '12',
                           },
        'textfont': {'color': '#FFFFFF',
                     'size': '12',
                     },
    }]
    layout = {
        'title': '<b>Purchased books by genre</b>',

    }
    return graph_values, layout


@app.route('/cart/customer_id/<book_name>', methods=['GET', 'POST'])
def cart(book_name):
    global user_name
    book_id = Book.get_id_by_username(book_name)
    author = Book.get_author_by_username(book_name)
    price = Book.get_price_by_username(book_name)
    genre = Book.get_genre_by_username(book_name)
    edition = Book.get_edition_by_username(book_name)
    Session = sessionmaker(bind=engine)
    session = Session()
    customer_id = Customer.get_id_by_username(user_name)

    temp = 0
    cart = session.query(Cart).filter(Cart.customer_id == customer_id).all()
    for book in cart:
        print(book.book_id)
        if book.book_id == book_id:
            temp += 1
    if temp > 0:
        flash('This book is already in your cart!!')
        return redirect(url_for('search'))
    cart = Cart(customer_id=customer_id, book_id=book_id, book_name=book_name, author=author,
                price=price, genre=genre, book_edition=edition)
    session.add(cart)
    session.commit()
    res = session.query(Cart).filter(Cart.customer_id == customer_id).all()
    session.flush()
    session.close()
    return render_template('shopping_cart.html', res=res, user_logged=user_logged, user_name=user_name)


@app.route('/cart/customer_id', methods=['GET'])
def view_cart():
    global user_name
    Session = sessionmaker(bind=engine)
    session = Session()
    customer_id = Customer.get_id_by_username(user_name)
    res = session.query(Cart).filter(Cart.customer_id == customer_id).all()
    session.flush()
    session.close()
    return render_template('shopping_cart.html', res=res, user_logged=user_logged, user_name=user_name)


@app.route('/book_page/prod/<id>', methods=['GET', 'POST'])
def book(id):
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(Book).filter(Book.book_id == id).first()
    session.flush()
    session.close()
    return render_template('book.html', res=res, user_logged=user_logged, user_name=user_name)


@app.route('/search', methods=['POST'])
def search():
    global user_name
    book_name = request.form['book_name']
    author = request.form['author']
    price = request.form['price']
    books = ""
    if book_name and author and price:
        Session = sessionmaker(bind=engine)
        session = Session()
        books = session.query(Book).filter(Book.book_name == book_name, Book.author == author, Book.price <= price)\
            .all()
        session.flush()
        session.close()
    form = BookForm()
    if not books:
        flash('No books wew found. Try another query!')
    return render_template('search.html', username=user_name, books=books, form=form, user_logged=user_logged,
                           user_name=user_name)


@app.route('/search', methods=['GET'])
def get_products():
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(Book).all()
    form = BookForm()
    session.flush()
    session.close()
    return render_template('search.html', products=res, form=form, user_logged=user_logged, user_name=user_name)


@app.route('/', methods=['GET', 'POST'])
def index():
    global current_page
    current_page = "main_page"
    return render_template('main_page.html', user_logged=user_logged, user_name=user_name,
                            first_name=first_name, second_name=second_name)


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html', user_logged=user_logged, user_name=user_name)


@app.route('/info/')
def info():
    return render_template('info.html', user_logged=user_logged, user_name=user_name)


@app.route('/graphs/')
def graphs():
    bar = create_plot()
    values, layout = create_pie()
    return render_template('graphs.html', plot=bar, graph_values=values, layout=layout, user_logged=user_logged,
                           user_name=user_name)


@app.route('/sign_in/')
def sign_in():
    form = LoginForm()
    return render_template('sign_in.html', form=form, user_logged=user_logged, user_name=user_name)


@app.route('/sign_up/')
def sign_up():
    form = RegisterForm()
    return render_template('sign_up.html', form=form, user_logged=user_logged, user_name=user_name)


@app.route('/login/submit', methods=['POST', 'GET'])
def login_submit():
    global user_name
    global first_name
    global second_name
    form = LoginForm()
    if form.is_submitted():
        global user_logged
        result = request.form

        user_id = Customer.perform_authorisation(result['login'], result['login_password'])
        if user_id == -1:
            flash('Wrong login or password!', 'error')
            return redirect(url_for('sign_in'))
        user_logged = True
        user_name = Customer.get_username(user_id)
        Session = sessionmaker(bind=engine)
        session = Session()
        res = session.query(Customer).filter(Customer.user_login == user_name).first()
        first_name = res.first_name
        second_name = res.second_name
        session.flush()
        session.close()
        return render_template('main_page.html', user_logged=user_logged, user_name=user_name,
                               first_name=first_name, second_name=second_name)
    return redirect(url_for('sign_in'))


@app.route('/registration/submit', methods=['POST', 'GET'])
def Register_submit():
    global user_name
    global user_logged
    global first_name
    global second_name
    form = RegisterForm()
    if form.is_submitted():
        result = request.form
        message = Customer.register_user(result['first_name'], result['second_name'], result['email'],
                                         result['user_login'], result['user_password'], result['confirm'])
        if message != 'Користувач усішно зареєстрований':
            flash('Wrong data or you already have an account!', 'error')
            return redirect(url_for('sign_up'))

        user_logged = True
        first_name = result['first_name']
        second_name = result['second_name']
        user_name = result['user_login']
        return render_template("main_page.html", user_logged=user_logged,
                                user_name=request.form['user_login'],
                                first_name=first_name, second_name=second_name)
    return redirect(url_for('sign_up'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', user_logged=user_logged, user_name=user_name), 404


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    global user_logged
    user_logged = False
    global user_name

    Session = sessionmaker(bind=engine)
    session = Session()
    customer_id = Customer.get_id_by_username(user_name)
    res = session.query(Cart).filter(Cart.customer_id == customer_id).all()
    if res:
        for elem in res:
            session.delete(elem)
            session.flush()
            session.commit()

    session.close()
    user_name = "Not Logged"
    return render_template("main_page.html", user_logged=user_logged, user_name=user_name)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    global user_name
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(Customer).filter(Customer.user_login == user_name).first()
    session.flush()
    session.close()
    # return render_template('index.html')

    # res = Customer.get_user_by_username(user_name)
    # print('glo', result)

    return render_template('profile.html', res=res, user_logged=user_logged, user_name=user_name)
