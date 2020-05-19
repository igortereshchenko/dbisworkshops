from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class UserForm(FlaskForm):
    user_id = StringField('User ID')
    user_first_name = StringField('User first name')
    user_last_name = StringField('User last name')
    user_email = StringField('User email')
    proceed = SubmitField('Submit')


class productForm(FlaskForm):
    product_id = StringField('Product_ID')
    product_name = StringField('Product')
    product_user_id = StringField('Product_user_id')
    proceed = SubmitField('Proceed')
