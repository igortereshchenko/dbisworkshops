from flask import request, render_template, redirect, abort, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from ..models import User
from .. import db
from ..forms import UserForm


def get_users_and_form():
    users = db.session.query(User)
    form = UserForm()
    return users, form


@app.route('/user', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    if first_name and last_name and email:
        existing_user = User.query.filter(User.email == email).first()
        if existing_user:
            return abort(400, 'User with such email already exist')

        new_user = User(first_name=first_name,
                        last_name=last_name,
                        email=email,
                        created=dt.now())

        db.session.add(new_user)
        db.session.commit()
    return redirect('/user')


@app.route('/user', methods=['GET'])
def get_all_users():
    users, form = get_users_and_form()
    return render_template('users.jinja2', users=users, form=form)


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db.session.query(User).filter(User.id == int(user_id)).delete()
    db.session.commit()

    return jsonify({}), 201
