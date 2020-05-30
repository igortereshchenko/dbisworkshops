from flask import Flask, render_template, url_for, redirect, request, session
from forms import SingInForm, ValidationForm, PurchaseForm, EventSelection, SuccessForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup import clients, events, guests
from flask_sqlalchemy import SQLAlchemy
import datetime
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bars'
oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'
app.config['SQLALCHEMY_DATABASE_URI'] = oracle_connection_string.format(

            username="SYSTEM",
            password="bars",
            sid="XE",
            host="localhost",
            port="1521",
            database="XE",
        )
db = SQLAlchemy(app)

global event_name
global event_time
global client_phone

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SingInForm()

    try:
        if form.is_submitted():
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

            engine = create_engine(oracle_connection_string.format(

                username="SYSTEM",
                password="bars",
                sid="XE",
                host="localhost",
                port="1521",
                database="XE",
            ), echo=True)

            Session = sessionmaker(bind=engine)
            session = Session()

            result = request.form
            adddata = clients(result['phone'], result['nickname'], result['password'], result['age'])
            session.add(adddata)
            session.commit()

            global client_phone
            client_phone = result['phone']

            return redirect(url_for('validation'))

    except Exception:
        return redirect(url_for('index'))

    return render_template('signin.html', form=form)

@app.route('/validation', methods = ['GET', 'POST'])
def validation():
    form = ValidationForm()
    if form.is_submitted():
        return redirect(url_for('select_event'))

    return render_template('validation.html', form=form)


@app.route('/select_event', methods=['GET', 'POST'])
def select_event():
    form = EventSelection()

    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

    engine = create_engine(oracle_connection_string.format(

        username="SYSTEM",
        password="bars",
        sid="XE",
        host="localhost",
        port="1521",
        database="XE",
    ), echo=True)

    with engine.connect() as conn:
        event_names = conn.execute("SELECT EVENT_NAME FROM EVENTS")
        form.event_name.choices += [(event, event) for event in event_names]

    if form.is_submitted():
        global event_name
        event_name = form.event_name.data
        return redirect(url_for('purchase'))

    return render_template('event_selection.html', form=form)

@app.route('/purchase', methods=['POST', 'GET'])
def purchase():
    form = PurchaseForm()

    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

    engine = create_engine(oracle_connection_string.format(

        username="SYSTEM",
        password="bars",
        sid="XE",
        host="localhost",
        port="1521",
        database="XE",
    ), echo=True)

    with engine.connect() as conn:
        global event_name
        event_name = re.search(r"[a-zA-z]+", event_name).group(0)
        price = conn.execute(
            "SELECT PRICE FROM EVENTS WHERE EVENT_NAME = '" + event_name + "'").fetchone()
        form.price.label = "price: " + str(price[0])

        tickets_left = conn.execute(
            "SELECT QUANTITY_TIC FROM EVENTS WHERE EVENT_NAME = '" + event_name + "'").fetchone()
        form.tickets_left.label = "tickets left: " + str(tickets_left[0])

        global event_time
        event_time = conn.execute(
            "SELECT EVENT_TIME FROM EVENTS WHERE EVENT_NAME = '" + event_name + "'").fetchone()
        form.event_time.label = "event time: " + str(event_time[0])

    if form.is_submitted():

        int_tickets_left = tickets_left[0] - 1

        with engine.connect() as conn:
            conn.execute("UPDATE events SET quantity_tic = " + str(int_tickets_left) + " WHERE event_name = '" + event_name + "'")
            global client_phone
            conn.execute(
                "INSERT INTO GUESTS(client_phone, event_name, event_time) VALUES('" + str(client_phone) + "', '" + str(
                    event_name) + "', " + "TO_DATE('" + str(event_time[0]) + "', 'YYYY-MM-DD HH24:MI:SS'))")

        return redirect(url_for('success'))

    return render_template('purchase.html', form=form)

@app.route("/success", methods=['GET', 'POST'])
def success():
    form = SuccessForm()

    if form.is_submitted():
        return redirect(url_for('index'))

    return render_template('ok.html', form=form)

if __name__ == '__main__':
   app.run()