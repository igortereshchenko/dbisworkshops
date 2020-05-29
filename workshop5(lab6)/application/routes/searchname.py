from flask import request, render_template, redirect, abort
from datetime import datetime as dt
from flask import current_app as app
from ..models import Product
from .. import db
from ..forms import ProductForm


@app.route('/searchname', methods=['POST'])
def show_product():

    name = request.form['name']
    price = request.form['price']

    if name and price:
        products = Product.query.filter(Product.name==name, Product.price <=price).all()



    form = ProductForm()
    return render_template('searchname.jinja2', products=products, form=form)


@app.route('/searchname', methods=['GET'])
def get_products():
    products = db.session.query(Product)
    form = ProductForm()
    return render_template('searchname.jinja2', products=products, form=form)
