from flask import Flask, render_template, request, redirect, url_for, abort, flash
from passlib.hash import sha256_crypt
from flask_fontawesome import FontAwesome
import datetime
from source.ORM_relations import Car, Driver, Wish, Services
from source.tryconn import d,c, g, create_plot

user_logged= False

user_name = "Not Logged"
iddd = 0
current_page = "home1"

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
fa = FontAwesome(app)


# if request.method == 'POST':
#     name = request.form.get('name')
#     username = request.form.get('username')
#     password = request.form.get('password')
#     confirm = request.form.get('confirm')
#     secure_password = sha256_crypt.encrypt(str(password))

@app.route('/')
def home_page():
    current_page ='home1'
    return render_template('home1.html', user_logged=user_logged, user_name=user_name, iddd = iddd)
@app.route('/services')
def services():
    current_page = 'services'
    return render_template('services.html', result = g, user_logged=user_logged, user_name=user_name, iddd = iddd)

@app.route('/services/find', methods = ['POST', 'GET'])
def services_find():
    if (request.method == 'POST'):
        find_serv_price = Services.search_service(request.form['namee'])
        print(find_serv_price)
        if find_serv_price==False:
            flash('No matches found')
            return render_template('services.html', result = list(zip(d,c)), user_logged=user_logged, user_name=user_name, iddd = iddd)
        else:
            g = find_serv_price
            return render_template("services.html", result=g, user_logged=user_logged, user_name=user_name,
                                   iddd=iddd)
    if (request.method == 'GET'):
        return redirect(url_for('services'))


@app.route('/contacts')
def contacts():
    current_page = 'contacts'
    return render_template('contacts.html', user_logged=user_logged, user_name=user_name, iddd = iddd)

@app.route('/reserve')
def reserve():
    current_page = 'reserve'
    return render_template('reserve.html', result = g, user_logged=user_logged, user_name=user_name, iddd = iddd)

@app.route('/reserve/make', methods = ['POST', 'GET'])
def reserve_make():
    if (request.method == 'POST'):
        date_diff = Wish.difference_between_dates(datetime.datetime.strptime(request.form['datetime'], '%Y-%m-%dT%H:%M'))
        if user_logged==False or iddd == 0:
            flash('Log in for reserving')
            return redirect(url_for('login'))
        elif date_diff == False:
            flash('You have to reserve at least one hour before coming')
            return render_template('reserve.html', result = g, user_logged=user_logged, user_name=user_name, iddd = iddd)
        else:
            date_is_busy = Wish.free_date(datetime.datetime.strptime(request.form['datetime'], '%Y-%m-%dT%H:%M'))
            if date_is_busy==False:
                Wish.add(request.form['service_name'], int(Wish.get_price(request.form['service_name'])),
                         datetime.datetime.strptime(request.form['datetime'], '%Y-%m-%dT%H:%M'), request.form['car_type'], iddd)
            else:
                msg = 'Date is taken by another driver'
                flash(msg)
                redirect(url_for('reserve'))


        return render_template(f"{current_page}.html", result = g, user_logged=user_logged, user_name=user_name, iddd = iddd)
    if(request.method == 'GET'):
        return redirect(url_for('reserve'))


@app.route('/register', methods = ['POST', 'GET'])
def register():
    return render_template('register.html', user_logged=user_logged, user_name=user_name, iddd = iddd)

@app.route('/register/submit', methods = ['POST', 'GET'])
def register_submit():
    global user_logged
    if(request.method == 'POST'):
        if request.form['password'] == request.form['confirm']:
            Driver.add(request.form['email'],request.form['first_name'],request.form['second_name'],
                       request.form['user_login'],request.form['password'],
                       datetime.datetime.strptime(request.form['birthday'], '%Y-%m-%d'), request.form['telephone'])
            Car.add(request.form['car_license_plate'],request.form['car_name'],str(request.form['car_type']),
                    request.form['car_color'])
        else:
            msg = 'You entered incorrect confirm password'
            flash(msg)
            return render_template('register.html', user_logged=user_logged, user_name=user_name, iddd = iddd)

        global current_page
        user_logged = True
        return render_template(f"{current_page}.html", user_logged=user_logged, user_name=request.form['user_login'], iddd = iddd)

    if(request.method == 'GET'):
        return redirect(url_for('register'))

@app.route('/login')
def login():
    return render_template('login.html', user_logged=user_logged, user_name=user_name, iddd = iddd)
@app.route('/login/submit', methods = ['POST', 'GET'])
def login_submit():
    if(request.method == 'POST'):
        global current_page
        global user_logged

        user_id = Driver.authorisation(request.form['login'],request.form['password'])
        if user_id == 0:
            # TODO Add notification
            msg = 'You didnt sign up yet'
            flash(msg)
            return redirect(url_for('login'))
        global iddd
        iddd = user_id
        user_logged = True
        global user_name
        user_name = Driver.get_username(user_id)
        return render_template(f"{current_page}.html",user_logged=user_logged, user_name=user_name,iddd = iddd)
    if(request.method == 'GET'):
        return redirect(url_for('login'), user_logged=user_logged, user_name=user_name, iddd = iddd)


@app.route('/logout', methods = ['POST', 'GET'])
def Logout():
    global current_page
    global user_logged
    user_logged = False
    global user_name
    global iddd
    iddd = 0
    user_name = "Not Logged"
    return render_template(f"{current_page}.html",user_logged=user_logged, user_name=user_name, iddd = iddd)
@app.route('/graph')
def graph():
    bar = create_plot()
    return render_template('graph.html', plot = bar, user_logged=user_logged, user_name=user_name, iddd = iddd)

@app.route('/<path>', methods = [ 'GET'])
def get(path):

   if path == "service":
      return redirect(url_for('services'))

   elif path == "contact":
      return redirect(url_for("contacts"))

   elif path == "reservation" or "book":
      return redirect(url_for("reserve"))
   else:
      return abort(404)




if __name__ == '__main__':
    service_discr = {
        'name' : 'Детейлинг мойка',
        'price_1_class': 30,
        'price_2_class': 70,
        'price_3_class': 100
    }
    driver = {
        'name' : 'Sasha',
        'birth_date': '12.02.1996',
        'telefon' : 23345676,
        'auto': 'Toyota Camry',
        'type_of_auto': '2_class',
        'color': 'black'
    }
    app.run(debug='True', port = 5003)