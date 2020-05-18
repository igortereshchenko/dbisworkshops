from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class UserForm(FlaskForm):
    first_name = StringField('User first name')
    last_name = StringField('User last name')
    email = StringField('User email')
    submit = SubmitField('Submit')


class GroupForm(FlaskForm):
    name = StringField('Dashboard name')
    submit = SubmitField('Submit')
