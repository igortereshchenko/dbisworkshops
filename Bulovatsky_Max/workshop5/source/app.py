from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import *
from forms import *

app = Flask(__name__)

os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://acfwdjeahlsvgl:e90c3e268016942f35a7650124a716365d0ad484c47b391f816ad7dc0e47e11d@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d1uae99vpu7qar"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'root'


db = SQLAlchemy(app)

cur_order = []




@app.route("/",  methods=['GET', 'POST'])
def hello():
    return render_template('index.html')



@app.route('/meal', methods=['GET', 'POST'])
def meal():
    meal_form = MealForm(request.form)

    if request.method == 'POST':

        meal_id = request.form['meal_id']
        name = request.form['name']
        price = request.form['price']
        taste = request.form['taste']
        risk_name = request.form['risk_name']

        try:
            meal = Meal(meal_id, name, price, taste, risk_name)
            db.session.add(meal)
            db.session.commit()

            return "Dish added {}".format(meal.meal_id)

        except Exception as e:
            return str(e)

    return render_template('meal.html', form=meal_form)



if __name__ == '__main__':
    app.run(debug=True)
