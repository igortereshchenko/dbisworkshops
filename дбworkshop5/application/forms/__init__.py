from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField


class UserForm(FlaskForm):
    first_name = StringField('User first name', [validators.required(), validators.length(max=32, min=2)])
    last_name = StringField('User last name', [validators.required(), validators.length(max=32, min=2)])
    email = StringField('User email', [validators.required(), validators.email()])
    submit = SubmitField('Submit')

class ProductForm(FlaskForm):
    name = StringField('Product name', [validators.required(), validators.length(max=32, min=2)])
    price = StringField('Product price', [validators.required(), validators.length(max=32, min=2)])
    submit = SubmitField('Submit')
    search = SubmitField('Search')


class UserBoughtProductsForm(FlaskForm):
    first_name = StringField('User first name', [validators.required(), validators.length(max=32, min=2)])
    last_name = StringField('User last name', [validators.required(), validators.length(max=32, min=2)])
    name = StringField('Product name', [validators.required(), validators.length(max=32, min=2)])
