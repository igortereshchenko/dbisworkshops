from flask import Flask, render_template, url_for, redirect, request, session
from forms import SingInForm, ValidationForm, PurchaseForm, EventSelection, SuccessForm, LoginForm, AdminForm, EventForm, AddEventForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup import clients, events, guests
from flask_sqlalchemy import SQLAlchemy
import datetime
import re
from bs4 import BeautifulSoup
import plotly.offline as py
import plotly.graph_objs as go
import cx_Oracle
import webbrowser

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


def stats():
    connection = cx_Oracle.connect("SYSTEM", "bars", "XE")

    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        EVENTS.EVENT_NAME,
        EVENTS.QUANTITY_TIC
     FROM
        EVENTS """)

    events = []
    quantity_tic = []

    for row in cursor:
        print("Event name: ", row[0], " and his quantity tic left: ", row[1])
        events += [row[0]]
        quantity_tic += [row[1]]

        data = [go.Bar(
            x=events,
            y=quantity_tic
        )]

        layout = go.Layout(
            title='Events and quantity tic left',
            xaxis=dict(
                title='Events',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=24,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                title='Quantity tic left',
                rangemode='nonnegative',
                autorange=True,
                titlefont=dict(
                    family='Courier New, monospace',
                    size=24,
                    color='#7f7f7f'
                )
            )
        )
    fig = go.Figure(data=data, layout=layout)

    py.plot(fig, auto_open=True)

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    try:
        if form.is_submitted():
            if form.signin.data:
                return redirect(url_for("signin"))

            result = request.form

            if result['nickname'] == 'admin' and result['password'] == 'admin':
                return redirect(url_for("admin"))

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
                check = conn.execute("SELECT 1 FROM clients WHERE client_phone = '" + result['nickname'] + "' AND client_pass = '" + result['password'] + "'").fetchone()
                if check[0] == 1:
                    global client_phone
                    client_phone = result['nickname']
                    return redirect(url_for("validation"))
                else:
                    raise Exception

    except Exception:
        return redirect(url_for("login"))

    return render_template("login.html", form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
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
        try:
            int_tickets_left = tickets_left[0] - 1

            with engine.connect() as conn:
                global client_phone
                conn.execute(
                    "INSERT INTO GUESTS(client_phone, event_name, event_time) VALUES('" + str(
                        client_phone) + "', '" + str(
                        event_name) + "', " + "TO_DATE('" + str(event_time[0]) + "', 'YYYY-MM-DD HH24:MI:SS'))")
                conn.execute("UPDATE events SET quantity_tic = " + str(int_tickets_left) + " WHERE event_name = '" + event_name + "'")


            return redirect(url_for('success'))

        except Exception:
            return redirect(url_for("select_event"))

    return render_template('purchase.html', form=form)

@app.route("/success", methods=['GET', 'POST'])
def success():
    form = SuccessForm()

    if form.is_submitted():
        return redirect(url_for('index'))

    return render_template('ok.html', form=form)

def TupleToDictionary(tuple):
    tmp, mydict = {}, []
    for rowproxy in tuple:
        for column, value in rowproxy.items():
            tmp = value
        mydict.append(tmp)

    return mydict

@app.route("/addevent", methods=['GET', 'POST'])
def addevent():
    form = AddEventForm()

    if form.is_submitted():
        try:
            oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

            engine = create_engine(oracle_connection_string.format(

                username="SYSTEM",
                password="bars",
                sid="XE",
                host="localhost",
                port="1521",
                database="XE",
            ), echo=True)

            result = request.form


            with engine.connect() as conn:
                conn.execute(
                    "INSERT INTO events (event_id, event_name, event_tag, reg_date_start, reg_date_finish, quantity_tic, event_time, price) VALUES (" +
                    result['event_id'] + ", '" + result['event_name'] + "', '" + result['event_tag'] + "', TO_DATE('" +
                    result['reg_date_start'] + "', 'YYYY-MM-DD HH24:MI:SS'), " + "TO_DATE('" +
                    result['reg_date_finish'] + "', 'YYYY-MM-DD HH24:MI:SS'), " + result['tickets_left'] + ", TO_DATE('" +
                    result['event_time'] + "', 'YYYY-MM-DD HH24:MI:SS'), " + result['price'] + ")")

                return redirect(url_for("admin"))

        except Exception as e:
            print(e)
            # return redirect(url_for("addevent"))

    return render_template("addevent.html", form=form)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    form = AdminForm()

    if form.is_submitted():
        if form.stats.data:
            stats()
            return redirect(url_for("admin"))

        return redirect(url_for("addevent"))

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
        events_count = conn.execute("SELECT COUNT(event_name) FROM EVENTS").fetchone()

        event_names = conn.execute("SELECT EVENT_NAME FROM EVENTS")
        tickets_left = conn.execute("SELECT QUANTITY_TIC FROM EVENTS")
        event_times = conn.execute("SELECT EVENT_TIME FROM EVENTS")
        prices = conn.execute("SELECT PRICE FROM EVENTS")

        dict_event_names = TupleToDictionary(event_names)
        dict_tickets_left = TupleToDictionary(tickets_left)
        dict_event_times = TupleToDictionary(event_times)
        dict_prices = TupleToDictionary(prices)

        event_forms = []

        for i in range(0, events_count[0]):
            event = EventForm()
            event.name.data = dict_event_names[i]
            event.tickets_left.data = dict_tickets_left[i]
            event.time.data = dict_event_times[i]
            event.price.data = dict_prices[i]

            event_forms.append(event)

        form.events = event_forms

    return render_template("admin.html", form=form)

@app.route('/delete/<string:id>')
def delete(id):
    oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{host}:{port}/{sid}'

    engine = create_engine(oracle_connection_string.format(

        username="SYSTEM",
        password="bars",
        sid="XE",
        host="localhost",
        port="1521",
        database="XE",
    ), echo=True)

    soup = BeautifulSoup(id, 'html.parser')
    val = soup.input['value']

    with engine.connect() as conn:
        conn.execute("DELETE FROM EVENTS WHERE EVENT_NAME = '" + val + "'")

    return redirect(url_for("admin"))

if __name__ == '__main__':
   app.run()
