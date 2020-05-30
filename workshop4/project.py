from flask import Flask
from flask import request
from flask import render_template

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Expenditure import Expenditure, Card
import sqlalchemy

from forms import ExpenditureForm, CreateCard

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pasha'


@app.route("/", methods=['GET'])
def hello():
    return (
        {
            "uri": "/",
            "sub_uri": {
                "user expenditure": "/index",
                "card creating": "/card",

            }
        }
    )


@app.route('/index', methods=["GET", "POST"])
def vitrati():
    form = ExpenditureForm()
    if form.is_submitted():
        # try:
        oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

        engine = create_engine(oracle_connection_string.format(

            username="SYSTEM",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT",
        ), echo=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        result = request.form
        adddata = Expenditure(result['cost_value'], result['time'], result['category_name'], result['card_number'])
        session.add(adddata)
        session.commit()
        return render_template('confirmIsOkey.html', result=result)

    # except:
    #	result = request.form
    #	return render_template('confirmIsNotOkey.html', result = result)

    return render_template('index.html', form=form)


@app.route('/card', methods=["GET", "POST"])
def tocreatecard():
    form = CreateCard()
    if form.is_submitted():
        # try:
        oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
        engine = create_engine(oracle_connection_string.format(

            username="SYSTEM",
            password="Oracle",
            sid="XE",
            host="localhost",
            port="1521",
            database="PROJECT"),
            echo=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        result = request.form
        adddata = Card(result['card_number'], result['money_amount'])
        session.add(adddata)
        session.commit()
        return render_template('confirmIsOkey.html', result=result)

    # except:
    #	result = request.form
    #	return render_template('confirmIsNotOkey.html', result = result)

    return render_template('card.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)