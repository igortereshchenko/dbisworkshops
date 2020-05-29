from flask import request, render_template, redirect, abort
from datetime import datetime as dt
from flask import current_app as app
from ..models import User_bought_products
from .. import db
from ..forms import UserBoughtProductsForm



@app.route('/user_bought_products', methods=['GET'])
def get_all_products_and_users():
    ubproducts = db.session.query(User_bought_products)
    form = UserBoughtProductsForm()
    return render_template('user_bought_products.jinja2', ubproducts=ubproducts, form=form)
