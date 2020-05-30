from flask import Flask, request, jsonify, redirect, url_for, render_template
from sqlalchemy.orm import sessionmaker
import cx_Oracle
from sqlalchemy import create_engine
from tables_db import Meal, Meal, MenuMeal, Risk, MealRisk
from forms import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(
    oracle_connection_string.format(

        username="SYS as sysdba",
        password="dbpass",
        sid="XE",
        host="laptop",
        port="1521",
        database="workshopDB"

    )
    , echo=True
)



meal_example = {
    "name": "Ice-cream",
    "price": 9.99
}

menu_example = {
    "name": "Lite summer kit",
    "content": ["MilkShake", "Ice-cream", "French fries"]
}

db = SQLAlchemy(app)

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




@app.route('/api/<action>', methods=['GET'])
def apiget(action):

   if action == "menu":
      return render_template("menu.html", menu=menu_example)

   elif action == "all":
      return render_template("all.html", meal=meal_example, menu=menu_example)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():


   # <button type="submit" form="form_meal" name="action" value="meal_update">Submit</button>
   # send name="action" and value="meal_update" to POST

    if request.form["action"] == "meal_update":

        meal_example["name"] = request.form["name"]
        meal_example["price"] = request.form["price"]

    elif request.form["action"] == "menu_update":

        menu_example["name"] = request.form["name"]
        menu_example["content"] = request.form["content"]

    return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':
    app.run()





