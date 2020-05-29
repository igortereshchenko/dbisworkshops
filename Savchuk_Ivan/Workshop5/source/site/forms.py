from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField


class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')
