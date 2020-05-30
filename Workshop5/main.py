from flask import Flask, render_template, request, redirect, url_for, flash
from forms.search_form import SearchToken
from dao.orm.model import *
from dao.db import OracleDb
from forms.user_form import RegistrationForm
from sqlalchemy.sql import func
from flask_bcrypt import Bcrypt
import random
import hashlib

import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go

import json

app = Flask(__name__)
app.secret_key = 'development key'
bcrypt = Bcrypt()
db = OracleDb()

@app.route('/')
def root():
    return render_template('index.html')

def hashing(user_id, user_name, user_surname, user_email, user_phone = 0):
    string = str(user_id) + str(user_name) + str(user_surname) + str(user_email) + str(user_phone)
    mix = ''.join(random.sample(string,len(string)))
    result = hashlib.sha256(mix.encode())
    return result.hexdigest()

@app.route('/signup', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.user_password.data).decode('utf-8')
        user = ormUser(user_name = form.user_name.data,
                        user_surname = form.user_surname.data,
                        user_email = form.user_email.data,
                        user_phone = form.user_phone.data,
                        user_password = hashed_password)
        token = ormToken(user_token = hashing(user.user_id, user.user_name, user.user_surname, user.user_email, user.user_phone))
        db.sqlalchemy_session.add_all([user, token])
        db.sqlalchemy_session.commit()
        flash(f'Token created: { token.user_token }', 'success')
        return redirect(url_for('root'))
    return render_template('signup.html', title = 'Register',form = form)

@app.route('/user', methods=['GET', 'POST'])
def user_table():
    result = db.sqlalchemy_session.query(ormUser).all()
    return render_template('users.html', users=result)

@app.route('/token', methods=['GET', 'POST'])
def token_table():
    result = db.sqlalchemy_session.query(ormToken).all()
    return render_template('token.html', tokens=result)

@app.route('/usertoken', methods=['GET', 'POST'])
def usertoken_table():
    result = db.sqlalchemy_session.query(ormUserToken).all()
    return render_template('usertoken.html', usertokens=result)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchToken()
    if form.validate_on_submit():
        user = ormToken.query.filter_by(user_token=form.user_token).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            result = db.sqlalchemy_session.query(ormUser.user_name,
                                                 ormUser.user_surname,
                                                 ormUser.user_email,
                                                 ormUser.user_phone,
                                                 ormUser.end_date)
            return render_template('result.html', personal_data=result)
        else:
            flash('Search Unsuccessful. Please check token and password', 'danger')
    return render_template('search.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def graph():
    # SELECT count(user_id), end_date
    # FROM USER_TABLE
    # GROUP BY END_DATE;

    query1 = (
        db.sqlalchemy_session.query(
            ormUser.end_date,
            func.count(ormUser.user_id).label('user_count')
        ).group_by(ormUser.end_date)
    ).all()

    date, user_counts = zip(*query1)
    bar = go.Bar(
        x=date,
        y=user_counts
    )

    data = {
        "bar": [bar],
    }

    graphsJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphsJSON)

if __name__ == '__main__':
    app.run(debug=True)
