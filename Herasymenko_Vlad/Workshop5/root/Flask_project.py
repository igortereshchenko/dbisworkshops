from flask import Flask, render_template, url_for, redirect, request, flash
from root.dao.data_classes import User,Material,Vendors,Bank,Vendor_Material,get_filtred_year_date
from flask_mail import Mail,Message

import plotly
import plotly.graph_objs as go
import plotly.express as px

import pandas as pd
import json



def create_plot(supplier,mat_id,year):
    if supplier == None:
        supplier = 39080209
    if mat_id == None:
        mat_id = 27
    if year == None:
        year = 2019

    x = ["січень","лютий","березень","квітень","травень","червень","липень","серпень","вересень","жовтень","листопад","грудень"]

    #y = get_filtred_year_date(2019,39080209,27)
    y,message = get_filtred_year_date(int(year), int(supplier), int(mat_id))

    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe

    mat_name = Material.get_mat_name(mat_id)
    vend_name = Vendors.get_vend_name(supplier)

    fig = go.Figure(
    data = [go.Bar(x=df['x'], # assign x as the dataframe column 'x'
            y=df['y'],
            marker_color='crimson')],
            layout_title_text=f'Зміна ціни за {year} рік на "{mat_name}" у "{vend_name}"',

    )



    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

user_logged= False

user_name = "Not Logged"

current_page = "Home"

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

app.config['MAIL_USERNAME'] = 'vladherr2020@gmail.com'
app.config['MAIL_PASSWORD'] ='roksolana2012'

mail = Mail(app)

material_list = []

app.secret_key = b'1488'

@app.route('/')
def Home():
    global current_page
    current_page = "Home"
    return render_template("Home.html",user_logged=user_logged, user_name=user_name)

@app.route('/materials/')
def Materials():

    name_pattern = request.args.get('search')
    id_list = Material.find_material_id(name_pattern)

    if id_list == [] and name_pattern != None:
        flash('Записів, на жаль, не знайдено')
    global material_list
    material_list = []
    if request.args.get('search') != None:
        for id in id_list:

            mat_name = Material.get_mat_name(id)

            vend_edrpous = Material.find_vend_edrpou(id)

            prices = []
            if vend_edrpous == []:
                vend_names = ['На жаль, поки інформації у базі даних немає']
                #continue
            else:
                vend_names = []

                for ed in vend_edrpous:
                    price = Material.get_vendors_price_globally(id,ed)
                    prices.append(price)
                    vend_names.append(Vendors.get_vend_name(ed))

            if prices != []:
                avg_price = sum(prices)/len(prices)
            else:
                avg_price = 'Недостатньо інформації'

            material_list.append((mat_name, vend_names,id,avg_price))
    else:
        id_list = Material.find_material_id('')

        for id in id_list:

            mat_name = Material.get_mat_name(id)

            vend_edrpous = Material.find_vend_edrpou(id)

            prices = []
            if vend_edrpous == []:
                vend_names = ['Інформація, на жаль, відсутня']
                #continue
            else:
                vend_names = []
                for ed in vend_edrpous:
                    price = Material.get_vendors_price_globally(id,ed)
                    prices.append(price)
                    vend_names.append(Vendors.get_vend_name(ed))

            if prices != []:
                avg_price = sum(prices)/len(prices)
            else: avg_price = 'Недостатньо інформації'

            material_list.append((mat_name, vend_names,id,avg_price))

    global current_page
    current_page = "Materials"

    if request.args.get('sort') != None:
        sort_method = request.args.get('sort')
    else:
        sort_method = "Name"

    if sort_method == 'Name':
        material_list = sorted(material_list, key=lambda t: t[0])

    if sort_method == 'Sup':
        material_list = sorted(material_list, key=lambda t: t[1][0])

    if name_pattern == None:
        name_pattern=''
    return render_template("Materials.html",user_logged=user_logged, user_name=user_name, material_list = material_list, name_pattern = name_pattern)


@app.route('/materials/prod/<id>')
def Material_page_handler(id):
    mat_name = Material.get_mat_name(id)
    vend_edrpous = Material.find_vend_edrpou(id)

    global current_material
    current_material = Material(id)

    prices = []
    suppliers = []
    if vend_edrpous == []:
        suppliers = [('Інформація, на жаль, відсутня', '')]
    else:
        for ed in vend_edrpous:
            price = current_material.get_vendors_price(ed)
            prices.append(price)
            suppliers.append((Vendors.get_vend_name(ed),price))

    if prices != []:
        avg_price = sum(prices)/len(prices)
    else:
        avg_price = 'Недостатньо інформації'
    description = current_material.get_mat_description()

    if description in [None,'']:
        description = 'Не вказано'

    return render_template("material_page.html",user_logged=user_logged,mat_name=mat_name, username=user_name,
                           suppliers = suppliers, description = description, avg_price = avg_price)

@app.route('/materials/delete/', methods= ['POST'])
def Material_deleter():
    if user_name == 'admin':
        msg = current_material.delete_material()
        flash(msg)
    return redirect(url_for('Materials'))

@app.route('/materials/add/', methods= ['GET'])
def Material_add_render():
    if user_name == 'admin':
        return render_template('add_material.html',user_logged=user_logged, username=user_name)
    else:
        flash('Тільки менеджер може додавати матеріали')
        return redirect(url_for('Materials'))

@app.route('/materials/add/submit/', methods= ['POST'])
def Material_adder():
    if user_name == 'admin':
        message_add = Material.add_material(request.form['mat_name'],request.form['description'])
        flash(message_add)
        return redirect(url_for('Materials'))
    else:
        flash('Тільки менеджер може додавати матеріали')
        return redirect(url_for('Materials'))

@app.route('/materials/update/', methods= ['POST'])
def Material_update_render():
    if user_name == 'admin':
        mat_name = current_material.get_self_name()
        return render_template('update_material.html',user_logged=user_logged, username=user_name,mat_name=mat_name)
    else:
        flash('Тільки менеджер може змінювати матеріали')
        return redirect(url_for('Materials'))

@app.route('/materials/update/submit/', methods= ['POST'])
def Material_update():
    if user_name == 'admin':
        if request.form['new_mat_name'] not in [None,'']:
            message = current_material.update_material(request.form['new_mat_name'])
            flash(message)
        if request.form['new_description'] not in [None,'']:
            message2 = current_material.update_material_description(request.form['new_description'])
        return redirect(url_for('Materials'))
    else:
        flash('Тільки менеджер може змінювати матеріали')
        return redirect(url_for('Materials'))

@app.route('/materials/send_email/', methods= ['GET'])
def Emailer():
    quantity = request.args.get('quantity')
    mat_name = current_material.get_self_name()
    supplier = str(request.args.get('supp'))

    mat_id = current_material.mat_id

    if supplier == 'Choose':
        return redirect(url_for('Materials'))
    return render_template('Bestellung.html',user_logged=user_logged, supplier= supplier, user_name=user_name,mat_name = mat_name,
                           quantity = quantity, mat_id = mat_id)

@app.route('/materials/send_email/submit', methods= ['POST'])
def Sender():

    msg = Message(body="Hello",
                  recipients=["8889344@ukr.net"],
                  sender='vladherr2020@gmail.com')

    mail.send(msg)
    return redirect(url_for('Materials'))



@app.route('/suppliers/')
def Suppliers():
    global current_page
    current_page = "Suppliers"


    name_pattern = request.args.get('search')
    ed_list = Vendors.get_edrpou(name_pattern)
    print(ed_list)
    if ed_list == [] and name_pattern != None:
        flash('На жаль, записів не знайдено')

    global supplier_list
    supplier_list = []
    if request.args.get('search') != None:
        for ed in ed_list:
            vend_name = Vendors.get_vend_name(ed)

            prod_list_ids = Vendors.get_products(ed)

            products = []
            for id in prod_list_ids:
                products.append(Material.get_mat_name(id))

            if products == []:
                products = ['На жаль, поки що інформації немає']

            roz_rah = Bank.get_bank_roz_rah(ed)

            supplier_list.append( (vend_name,products,ed,roz_rah) )
    else:
        ed_list = Vendors.get_edrpou('')

        for ed in ed_list:

            vend_name = Vendors.get_vend_name(ed)

            prod_list_ids = Vendors.get_products(ed)

            products = []
            for id in prod_list_ids:
                products.append(Material.get_mat_name(id))

            if products == []:
                products = ['На жаль, поки що інформації немає']

            roz_rah = Bank.get_bank_roz_rah(ed)

            supplier_list.append( (vend_name,products,ed,roz_rah) )

    if request.args.get('sort') != None:
        sort_method = request.args.get('sort')
    else:
        sort_method = "Name"

    if sort_method == 'Name':
        supplier_list = sorted(supplier_list, key=lambda t: t[0])

    if sort_method == 'Ed':
        supplier_list = sorted(supplier_list, key=lambda t: t[2])

    if name_pattern == None:
        name_pattern=''

    print(supplier_list)
    return render_template("Suppliers.html",user_logged=user_logged, user_name=user_name, suppliers_list = supplier_list,name_pattern =name_pattern)

@app.route('/suppliers/record/<ed>')
def Supplier_page_handler(ed):
    vend_name = Vendors.get_vend_name(ed)

    prod_list_ids = Vendors.get_products(ed)

    global current_supplier
    current_supplier = Vendors(ed)


    products = []

    if prod_list_ids == []:
        products = [(('Інформація, на жаль, відсутня',-1),'-')]
    else:
        for id in prod_list_ids:
            products.append(((Material.get_mat_name(id),id),Material.get_mat_price(id,ed)))

    vend_city = Vendors.get_vend_city(ed)
    vend_address = Vendors.get_vend_adress(ed)
    vend_email = Vendors.get_vend_email(ed)
    vend_tel = Vendors.get_vend_tel(ed)
    vend_m_name = Vendors.get_vend_m_name(ed)
    vend_ed = ed
    roz_rah = Bank.get_bank_roz_rah(ed)
    bank_name = Vendor_Material.get_bank_name(ed)
    mfo = Vendor_Material.get_bank_mfo(int(ed))
    details = [vend_city,vend_address,vend_email,vend_tel,vend_m_name,vend_ed,roz_rah,bank_name, mfo]


    return render_template("supplier_page.html",user_logged=user_logged, user_name=user_name,materials = products, details = details, sup_name = vend_name)

@app.route('/suppliers/add/')
def Add_sup():
    if user_name == 'admin':
        return render_template('add_supplier.html',user_logged=user_logged, user_name=user_name)
    else:
        flash('Тільки менеджер може додавати постачальників')
        return redirect(url_for('Suppliers'))

@app.route('/suppliers/add/submit', methods= ['POST'])
def Create_sup_record():
    if user_name == 'admin':

        message1 = Vendors.add_vendor(request.form['sup_name'],request.form['ed'],request.form['adr'],request.form['city'],request.form['tel'],request.form['m_name'],
                           request.form['email'])

        message2 = Bank.add_bank(request.form['bank_name'],request.form['rr'],request.form['mfo'],request.form['ed'])

        flash(message1)
        flash(message2)
        return redirect(url_for('Suppliers'))
    else:
        flash("Тільки менеджер може додавати постачальників")
        return redirect(url_for('Suppliers'))

@app.route('/suppliers/delete/', methods= ['POST'])
def Supplier_deleter():
    if user_name == 'admin':
        message = current_supplier.delete_vendor()
        flash(message)
    return redirect(url_for('Suppliers'))


@app.route('/suppliers/add_vend_mat', methods= ['POST'])
def Supplier_add_vend_mat():
    if user_name == 'admin':

        name_pattern = request.form['mat_name']
        id_list = Material.find_material_id(name_pattern)
        if id_list != []:
            msg = Vendor_Material.add_vend_mat(id_list[0],current_supplier.v_edrpou,request.form['price'])
            if msg != 'Запис додано успішно':
                flash(msg)
        else:
            msg_add = Material.add_material(request.form['mat_name'],None)
            if msg_add != 'Введено невірні дані!' and msg_add !='Запис додано успішно':
                id = Material.find_material_id(request.form['mat_name'])[0]
                msg = Vendor_Material.add_vend_mat(id,current_supplier.v_edrpou,request.form['price'])
            else:
                flash(msg_add)


    return redirect(url_for('Supplier_page_handler', ed = current_supplier.v_edrpou))

@app.route('/suppliers/delete_vend_mat/<id>', methods= ['POST'])
def delete_sup_vend_mat(id):
    if user_name == 'admin':
        message = Vendor_Material.delete_vend_mat(id,current_supplier.v_edrpou)

    return redirect(url_for('Supplier_page_handler', ed = current_supplier.v_edrpou))

@app.route('/suppliers/update/', methods= ['POST'])
def Supplier_updater():
    if user_name == 'admin':
        ed = current_supplier.v_edrpou

        vend_name = Vendors.get_vend_name(ed)
        vend_city = Vendors.get_vend_city(ed)
        vend_address = Vendors.get_vend_adress(ed)
        vend_email = Vendors.get_vend_email(ed)
        vend_tel = Vendors.get_vend_tel(ed)
        vend_m_name = Vendors.get_vend_m_name(ed)
        roz_rah = Bank.get_bank_roz_rah(ed)

        return render_template("update_supplier.html", user_logged=user_logged, user_name=user_name, sup_name = vend_name, city = vend_city,
                               adr = vend_address, email = vend_email, m_name = vend_m_name,
                               roz_rah = roz_rah)
    else:
        flash('Тільки менеджер може оновлювати записи')
        return redirect(url_for('Suppliers'))

@app.route('/suppliers/update/submit', methods= ['POST'])
def Supplier_updater_submit():
    if user_name == 'admin':
        ed = current_supplier.v_edrpou
        msg1 = current_supplier.update_vendor(request.form['new_sup_name'],request.form['new_adr'],request.form['new_city'],
                                       request.form['new_tel'],request.form['new_m_name'],request.form['new_email'])

        msg2 = Bank.update_bank(request.form['bank_name'],request.form['rr'],request.form['mfo'],ed)

        flash(msg1)


        if msg2 != 'Запис успішно оновлено!':

            msg3 = Bank.add_bank(request.form['bank_name'],request.form['rr'],request.form['mfo'],ed)
            flash(msg3)
        else:
            flash(msg2)

    return redirect(url_for('Suppliers'))

@app.route('/dynamic/', methods=['GET'])
def Dynamic():
    global current_page
    current_page = "Dynamic"
    supplier_name_pattern = request.args.get('supp')
    material_name_pattern = request.args.get('products')
    year = request.args.get('year')

    ed_list = Vendors.get_edrpou(supplier_name_pattern)
    id_list = Material.find_material_id(material_name_pattern)

    if supplier_name_pattern == None or ed_list == []:
        supplier = 39080209
    else:
        supplier = ed_list[0]

    if material_name_pattern == None or id_list == []:
        mat_id = 27
    else:
        mat_id = id_list[0]

    bar = create_plot(supplier,mat_id,year)

    return render_template("Dynamic.html",user_logged=user_logged, user_name=user_name, plot=bar)

@app.route('/login/')
def Log():
    return render_template("LogIn.html")


@app.route('/registration/')
def Register():
    return render_template("Reg.html")

@app.route('/registration/submit', methods = ['POST', 'GET'])
def Register_submit():
    if(request.method == 'POST'):
        message = User.register_user(request.form['name'],request.form['Email'],request.form['pass'],request.form['pass_val'])

        if message != 'Користувач усішно зареєстрований':
            flash(message)
            return redirect(url_for('Register'))

        else:
            global user_logged
            global current_page
            user_logged = True
            return render_template(f"{current_page}.html",user_logged=user_logged, user_name=request.form['name'])

    if(request.method == 'GET'):
        return redirect(url_for('Register'))


@app.route('/login/submit', methods = ['POST', 'GET'])
def Log_submit():
    if(request.method == 'POST'):
        global current_page
        global user_logged

        user_id = User.perform_authorisation(request.form['name'],request.form['pass'])
        if user_id == -1:
            flash(" Не вірний логін користувача чи пароль")
            return redirect(url_for('Log'))

        user_logged = True
        global user_name
        user_name = User.get_username(user_id)
        return render_template(f"{current_page}.html",user_logged=user_logged, user_name=user_name)
    if(request.method == 'GET'):
        return redirect(url_for('Log'))

@app.route('/logout', methods = ['POST', 'GET'])
def Logout():
    global current_page
    global user_logged
    user_logged = False
    global user_name
    user_name = "Not Logged"
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
