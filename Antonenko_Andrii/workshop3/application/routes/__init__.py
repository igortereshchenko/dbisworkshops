from flask import request, render_template, make_response, abort
from datetime import datetime as dt
from flask import current_app as app
from ..models import User
from .. import db


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
    return make_response('Success')
