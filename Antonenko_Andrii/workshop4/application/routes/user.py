from flask import request, render_template, redirect, abort, jsonify
from datetime import datetime as dt
from flask import current_app as app
from ..models import User, User_Group
from .. import db
from ..forms import UserForm


@app.route('/user', methods=['POST'])
def create_user():
    """Create a user via query string parameters."""
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
    users = db.session.query(User)
    form = UserForm()
    return render_template('users.jinja2', users=users, form=form)


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    # We need to add CASCADE deleting instead of
    db.session.query(User_Group).filter(User_Group.user_id == int(user_id)).delete()
    db.session.query(User).filter(User.id == int(user_id)).delete()
    db.session.commit()

    return jsonify(redirect=request.host + '/user'), 201
