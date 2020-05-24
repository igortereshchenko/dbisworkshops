from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField


class LoginForm(FlaskForm):
    username = StringField('Username: ', validators=[validators.DataRequired('Required')])
    password = PasswordField('Password: ', validators=[validators.DataRequired('Required')])

    submit = SubmitField('Sign in')
