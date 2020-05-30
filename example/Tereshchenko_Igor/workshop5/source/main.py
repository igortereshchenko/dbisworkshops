from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from root.source.ORM_relations import *
from root.source.items_model import items_model
from root.source.payments_model import payments_model
from root.source.user_model import *


app = Flask(__name__)
app.secret_key = "s_key"
app.config['SESSION_TYPE'] = 'filesystem'



@app.route('/')
def login():
    return redirect("/singin", code=302)

@app.route('/<page>', methods = ['GET', 'POST'])
def singup(page):
    if page == 'singin':
        # redirect if already login
        if session and session['user']:
            return redirect("/settings", code=302)

        # try to login
        if request.method == 'POST':
            login = request.form['login'].strip()
            password = request.form['password'].strip()

            # check user in DB
            user = user_model.login(login, password)

            # check if there is any mistakes
            if isinstance(user, str):
                return render_template("login.html", usr_error=user)

            # login and redirect to settings
            else:
                session['user'] = user[0][0]
                return redirect("/settings", code=302)
        else:
            return render_template("login.html")

    elif page == 'singup':
        # redirect if already login
        if session and session['user']:
            return redirect("/settings", code=302)

        # try to sing up
        if request.method == 'POST':
            login = request.form['login']
            password = request.form['password']

            # sing up
            user = user_model.add(login, password)

            # if there is no similar users - redirect
            if(user):
                session['user'] = user.id
                return redirect("/settings", code=302)

            # notification about similar username
            else:
                usr_error = "Такой пользователь уже существует."
                return render_template("singup.html", usr_error=usr_error)
        else:
            return render_template("singup.html")

    elif page == 'settings':
        # redirect if user are logged
        if not session or not session['user']:
            return redirect("/singin", code=302)

        if request.method == 'POST':
            profit_percent = request.form['profit_percent']
            min_price = request.form['min_price']
            max_price = request.form['max_price']
            sls_per_day = request.form['sls_per_day']
            balance_to_stop = request.form['balance_to_stop']
            max_items_in_inventory = request.form['max_items_in_inventory']

            config_answr = user_model.setConfig(session['user'], profit_percent, min_price, max_price, sls_per_day, balance_to_stop, max_items_in_inventory)


            # check if there is any mistakes
            if isinstance(config_answr, str):
                config = user_model.getConfig(session['user'])
                return render_template("settings.html", config_error=config_answr, config=config)

            else:
                config = user_model.getConfig(session['user'])
                return render_template("settings.html", config=config)


        else:
            config = user_model.getConfig(session['user'])
            return render_template("settings.html", config=config)

    elif page == 'payments':
        # redirect if user are logged
        if not session or not session['user']:
            return redirect("/singin", code=302)

        balance = payments_model.getBalance(session['user'])

        if request.method == 'POST':
            summary = request.form['summary']
            withdraw_errors = payments_model.withdrawBalance(session['user'], summary)

            if isinstance(withdraw_errors, str):
                return render_template("payments.html", balance=balance, payment_error=withdraw_errors)
                pass
            else:
                balance = payments_model.getBalance(session['user'])

                return render_template("payments.html", balance=balance)
        else:
            return render_template("payments.html", balance=balance)


    elif page == 'main':
        # redirect if user are logged
        if not session or not session['user']:
            return redirect("/singin", code=302)

        config = user_model.getConfig(session['user'])
        items = items_model.checkItems(session['user'], config, guns)

        return render_template("statistic.html", items=items, time=datetime.now().strftime("%Y-%m-%d"))





    elif page == 'logout':
        # redirect if user are logged
        if session and session['user']:
            # log out
            session.pop('user', None)

        return redirect("/singin", code=302)

    else:
        return render_template("404.html")






if __name__ == '__main__':
    # db = OracleDb()
    user_model()
    guns = [
       {
           "gun_name": "AK-47",
           "gun_price": 10,
           "gun_average_price": 12,
           "daily_sales": 100,
       },
       {
           "gun_name": "M4S1",
           "gun_price": 8,
           "gun_average_price": 12,
           "daily_sales": 1,
       },
       {
           "gun_name": "AWP",
           "gun_price": 14,
           "gun_average_price": 12,
           "daily_sales": 100,
       },
       {
           "gun_name": "UMP-45",
           "gun_price": 10.5,
           "gun_average_price": 12,
           "daily_sales": 50,
       }
    ]

    app.run(debug=True)
    # app.run()