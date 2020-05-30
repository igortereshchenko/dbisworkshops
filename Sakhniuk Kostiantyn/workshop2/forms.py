from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ProductForm(FlaskForm):
    product_name = StringField('product_name')
    type = StringField('type')
    vendor = StringField('vendor')
    cost = StringField('cost')
    submit = SubmitField('Submit')

class VendorForm(FlaskForm):
    vendor_name = StringField('vendor_name')
    products = StringField('products')
    link = StringField('link')
    submit = SubmitField('Submit')