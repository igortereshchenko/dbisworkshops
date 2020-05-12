from flask import Flask, render_template, request, redirect, url_for, abort
from passlib.hash import sha256_crypt
from flask_fontawesome import FontAwesome
app = Flask(__name__, template_folder='C:\\Users\\38073\\Desktop\\Borozniuk_Dmytro\\workshop\\source\\templates', static_folder='C:\\Users\\38073\\Desktop\\Borozniuk_Dmytro\\workshop\\source\\static')
fa = FontAwesome(app)
@app.route('/')
def home_page():
    return render_template('home1.html')
@app.route('/services')
def services():
    return render_template('services.html', result = service_discr)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/reserve')
def reserve():
    return render_template('reserve.html')

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        secure_password = sha256_crypt.encrypt(str(password))

    return render_template('register.html')

@app.route('/register/submit', methods = ['POST', 'GET'])
def register_submit():
    if(request.method == 'POST'):
        return "User has entered:"+str(request.form['name'])+ ' ' + str(request.form['username'])+ ' ' + str(request.form['password'])+ ' ' + str(request.form['confirm'])
    if(request.method == 'GET'):
        return redirect(url_for('register'))

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/login/submit', methods = ['POST', 'GET'])
def login_submit():
    if(request.method == 'POST'):
        return "User has entered:"+ ' ' + str(request.form['name'])+ ' ' + str(request.form['password'])
    if(request.method == 'GET'):
        return redirect(url_for('login'))

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
    app.run(debug='True')