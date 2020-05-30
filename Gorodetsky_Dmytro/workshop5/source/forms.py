from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from wtforms.fields.html5 import EmailField


class RegisterForm(FlaskForm):
    first_name = StringField('First name', [validators.required()])
    second_name = StringField('Last name', [validators.required()])
    email = EmailField('Email', [validators.required(), validators.Email()])
    user_login = StringField('Login', [validators.required()])
    user_password = PasswordField('Password', [
        validators.required(),
        validators.EqualTo('confirm')
    ])
    confirm = PasswordField('Confirm', [
        validators.required()
    ])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    login = StringField('Login', [validators.required()])
    login_password = PasswordField('Password', [
        validators.required()
    ])
    submit = SubmitField('Submit')


class BookForm(FlaskForm):
    book_name = StringField('Book name', [validators.required(), validators.length(max=32, min=1)])
    author = StringField('Book author', [validators.required(), validators.length(max=32, min=1)])
    price = StringField('Max book price', [validators.required(), validators.length(max=32, min=1)])
    search = SubmitField('Search')