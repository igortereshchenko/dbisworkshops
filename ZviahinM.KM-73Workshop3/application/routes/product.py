from flask import request, render_template, redirect, abort
from datetime import datetime as dt
from flask import current_app as app
from ..models import Product
from .. import db
from ..forms import ProductForm


@app.route('/product', methods=['POST'])
def add_product():

    name = request.form['name']
    price = request.form['price']
    
    if name and price:
        existing_product = Product.query.filter(Product.name == name).first()
        if existing_product:
            return abort(400, 'Product with such name already exist')
        new_product = Product(name=name,
                              price=price,
                              created=dt.now())
        db.session.add(new_product)
        db.session.commit()
        
    return redirect('/product')


@app.route('/product', methods=['GET'])
def get_all_products():
    products = db.session.query(Product)
    form = ProductForm()
    return render_template('product.jinja2', products=products, form=form)
