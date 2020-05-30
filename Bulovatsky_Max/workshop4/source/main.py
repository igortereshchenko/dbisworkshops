from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
import cx_Oracle
from sqlalchemy import create_engine
from tables_db import menu, meal, menu_meal, risk, meal_risk
from forms import *

app = Flask(__name__)


meal_example = {
    "name": "Ice-cream",
    "price": 9.99
}

menu_example = {
    "name": "Lite summer kit",
    "content": ["MilkShake", "Ice-cream", "French fries"]
}


@app.route('/')
def index():

    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

    engine = create_engine(oracle_connection_string.format(

        username="SYS as sysdba",
        password="dbpass",
        sid="XE",
        host="laptop",
        port="1521",
        database="workshopDB"
    ), echo=True)

    Session = sessionmaker(bind=engine)

    return render_template("meal.html", form=DishForm())


@app.route('/api/<action>', methods=['GET'])
def apiget(action):

   if action == "meal":
      return render_template("meal.html", meal=meal_example)

   elif action == "menu":
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





