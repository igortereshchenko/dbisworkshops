from flask import Flask, render_template, url_for, redirect, request

global user_logged
user_logged= False
global user_name
user_name = "Not Logged"
global current_page
current_page = "Home"

app = Flask(__name__)



material_list = [("Material_1","description"),("Material_2","description"),("Material_3","description"),("Material_4","description")]

global vendor
vendor = {
  "Назва фірми": "AGENT",
  "ЄДРПОУ": 41115963,
  "Адреса": "вул. Хвойка Вікентія, буд. 18/14, оф. 326",
  "Місто": "Київ",
  "Телефон": "+38(066) 100 20 07",
  "E-mail": "agentbud007@gmail.com"
}

global bank_name
bank_name = 'bank'

global vendor_name
vendor_name = 'vendor'


global bank
bank = {
  "Назва банку": "KYIV_CITY",
  "ЄДРПОУ": 41115963,
  "Розрахунковий рахунок": 26006056126373,
  "МФО": 380775,
    }


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',user_logged=user_logged, action = action, bank_name = bank_name, vendor_name = vendor_name), 404

@app.route('/api/<action>', methods = ['POST', 'GET'])
def workshop(action):

    if action == bank_name:
        return render_template("vendor.html", vendor = vendor)
    elif action == vendor_name:
        return render_template("bank.html", bank = bank)
    
    elif action == 'all':
        return render_template("all.html",user_logged=user_logged, user_name=user_name, vendor = vendor, bank = bank)

    else:
        return render_template('404.html',user_logged=user_logged, action = action, bank_name = bank_name, vendor_name = vendor_name), 404

@app.route('/api/KYIV_CITY/submit', methods = ['POST', 'GET'])
def workshop_bank_submit():
    if request.method == "POST":
        global bank
        bank["Назва банку"] = request.form['name']
        bank["ЄДРПОУ"] = request.form['ed']
        bank["Розрахунковий рахунок"] = request.form['pass']
        bank["МФО"] = request.form['mfo']
        return render_template("all.html",user_logged=user_logged, user_name=user_name, vendor = vendor, bank = bank)
    else:
        return render_template("bank.html", bank = bank)

@app.route('/api/AGENT/submit', methods = ['POST', 'GET'])
def workshop_vendor_submit():
    if request.method == "POST":
        global vendor
        vendor["Назва фірми"] = request.form['name']
        vendor["ЄДРПОУ"] = request.form['ed']
        vendor["Адреса"] = request.form['adr']
        vendor["Місто"] = request.form['city']
        vendor["Телефон"] = request.form['tel']
        vendor["E-mail"] = request.form['e_mail']
        
        return render_template("all.html",user_logged=user_logged, user_name=user_name, vendor = vendor, bank = bank)
    else:
        return render_template("bank.html", vendor = vendor)    


@app.route('/')
def Home():
    global current_page
    current_page = "Home"
    return render_template("Home.html",user_logged=user_logged, user_name=user_name)

@app.route('/materials/')
def Materials():
    global current_page
    current_page = "Materials"
    return render_template("Materials.html",user_logged=user_logged, user_name=user_name, material_list = material_list)

@app.route('/suppliers/')
def Suppliers():
    global current_page
    current_page = "Suppliers"
    return render_template("Suppliers.html",user_logged=user_logged, user_name=user_name)

@app.route('/dynamic/')
def Dynamic():
    global current_page
    current_page = "Dynamic"
    return render_template("Dynamic.html",user_logged=user_logged, user_name=user_name)

@app.route('/login/')
def Log():
    return render_template("LogIn.html")


@app.route('/registration/')
def Register():
    return render_template("Reg.html")

@app.route('/registration/submit', methods = ['POST', 'GET'])
def Register_submit():
    if(request.method == 'POST'):
        return "Користувач ввів"+str(request.form['Email'])+str(request.form['name'])+str(request.form['pass'])+str(request.form['pass_val'])
    if(request.method == 'GET'):
        return redirect(url_for('Register'))


@app.route('/login/submit', methods = ['POST', 'GET'])
def Log_submit():
    if(request.method == 'POST'):
        global current_page
        global user_logged
        user_logged = True
        global user_name
        name = request.form['name']
        user_name = name
        return render_template(f"{current_page}.html",user_logged=user_logged, user_name=user_name)
    if(request.method == 'GET'):
        return redirect(url_for('Log'))

@app.route('/logout', methods = ['POST', 'GET'])
def Logout():
    global current_page
    global user_logged
    user_logged = False
    global user_name
    name = "Not Logged"
    return render_template(f"{current_page}.html",user_logged=user_logged, user_name=user_name)

    
@app.route('/<path:path_route>')
def Search_path(path_route):
    if (path_route == 'prices' or path_route == 'price'):
        return redirect(url_for('Dynamic'))
    elif (path_route == 'supply' or path_route == 'supplier'):
        return redirect(url_for('Suppliers'))
    elif (path_route == 'material'):
        return redirect(url_for('Materials'))
    else:
        return render_template("WIP.html",paths=path_route,user_logged=user_logged, user_name=user_name)
        


if __name__ == '__main__':
   app.run(port = 5000)
