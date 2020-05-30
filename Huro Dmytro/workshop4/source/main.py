from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms.dish import DishAddForm
from forms.order import OrderAddForm
# from dao import db_api
from orm.database_connection import ENGINE_PATH_WIN_AUTH
from orm.create_table import Dishes, Orders
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ENGINE_PATH_WIN_AUTH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'


db = SQLAlchemy(app)


@app.route('/', methods = ['GET','POST'])
def index():

    return render_template('index.html')

@app.route('/dish', methods=['GET', 'POST'])
def dish():
    form_dish = DishAddForm(request.form)

    if request.method == 'POST':
        print(request.form['dish_name'])
        print(form_dish.validate())
        print(form_dish.errors)
        if form_dish.validate():
            #add by cx_oracle
            # db_api.new_dish(request.form['dish_name'],
            #                 request.form['dish_price'],
            #                 request.form['dish_describe'])
            # #add by orm
            db.session.add(Dishes(dish_name = request.form['dish_name'],
                                    dish_price = request.form['dish_price'],
                                    dish_describe = request.form['dish_describe']))
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('dish.html', form_dish=form_dish)


    return render_template('dish.html', form_dish=form_dish)

@app.route('/order', methods=['GET', 'POST'])
def order():
    form_order = OrderAddForm(request.form)
    
    if request.method == 'POST':
        print(request.form['dish_id'])
        print(form_order.validate())
        print(form_order.errors)
        if form_order.validate():
            #add by cx_oracle
            # db_api.new_order(request.form['dish_id'],
            #                 request.form['user_phone'],
            #                 request.form['user_name'],
            #                 request.form['amount_dishes'])
            # #add by orm
            db.session.add(Orders(dish_id = int(request.form['dish_id']),
                                    user_phone=request.form['user_phone'],
                                    user_name=request.form['user_name'],
                                    amount_dishes = request.form['amount_dishes']))
            db.session.commit()
            return redirect(url_for('index'))
        else:

            return render_template('order.html', form_order=form_order)


    return render_template('order.html', form_order=form_order)
if __name__ == '__main__':
    app.run(debug=True)