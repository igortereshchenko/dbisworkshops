#D:\КПИ\3КУРС\6Й СЕМЕСТР\DB_Project

from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from models import Dishes, Cafes, Orders, Queue
from forms.dish import DishAddForm
from forms.cafe import CafeAddForm
from forms.item_order import AddToOrder
from forms.order import CleanOrder, PushOrder, Cancel, Purchase

app = Flask(__name__)

os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://amsurmxifnypqr:4cc7d28e000594fe2351c7f7d04df59ef3cea9347b9028b33e8d262035b12b5a@ec2-54-247-79-178.eu-west-1.compute.amazonaws.com:5432/d4708p9ktk4c5u"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'root'

db = SQLAlchemy(app)

db.session.query(Queue).delete()
db.session.query(Orders).delete()
db.session.commit()

cur_order = []
cur_cafe = 0
cur_order_id = 1
flag_push = False
order_sum = 0
min_order_sum = 100
order_time = 0

@app.route("/",  methods=['GET', 'POST'])
def hello():
    return render_template('index.html')


@app.route("/order-food", methods=['GET', 'POST'])
def ord_food():
    cafes = db.session.query(Cafes).all()
    table = [(cafe.cafe_id, cafe.cafe_name) for cafe in cafes]
    return render_template('order.html', table=table, cur_cafe=cur_cafe)


@app.route("/cafe<id>",  methods=['GET', 'POST'])
def ord_food_cafe(id):
    table = [(x.dish_id, x.dish_name, x.dish_price, x.dish_describe)
             for x in db.session.query(Dishes).filter_by(cafe_id=id)]

    return render_template('cafe_menu.html', menu=table, cafe_id=id, form=AddToOrder(request.form))


@app.route("/queues",  methods=['GET', 'POST'])
def queues():
    cafes = db.session.query(Cafes).all()
    qu = db.session.query(Queue).all()
    names = [(cafe.cafe_id, cafe.cafe_name) for cafe in cafes]
    ques = [(q.queue_index, q.order_time, q.orders.cafe_id) for q in qu]
    left = []
    print(names)
    for c_id in names:
        cur=0
        for ordr in ques:
            if c_id[0] == ordr[2]:
                cur+=ordr[1]
        left.append(cur)

    return render_template('queues.html', cafes=names, queues=ques, left=left)


@app.route("/temp",  methods=['GET', 'POST'])
def order():
    global cur_cafe
    global cur_order_id
    global order_sum
    global order_time
    if request.method == 'POST':

        cafe_id = int(request.form['cafe_id'])
        cafe = db.session.query(Cafes).filter_by(cafe_id=cafe_id)[0]
        dish_id = int(request.form['item_id'])
        dish_num = int(request.form['item_amount'])
        dish = db.session.query(Dishes).filter_by(dish_id=dish_id)[0]
        cafe_id = int(dish.cafe_id)
        avg_time = float(dish.dish_avg_time)

        if len(cur_order) == 0:
            cur_cafe = cafe_id
        print(cur_cafe)
        ord = Orders(cur_order_id, dish_id, cafe_id, dish_num, avg_time)
        cur_order.append(ord)
        order_sum += dish_num*dish.dish_price
        order_time += avg_time*dish_num
    return render_template('temp.html', cafe=[cafe_id, cafe.cafe_name], dish=[dish.dish_name, dish_num])


@app.route("/order_accepted",  methods=['GET', 'POST'])
def order_accepted():
    global cur_order_id
    global cur_order
    global order_sum
    global cur_cafe
    global order_time

    if request.method == 'POST' and len(cur_order) != 0:
        time = 0
        for o in cur_order:
            db.session.add(o)
            time += o.amount_dishes * o.avg_time

        q = Queue(cur_order_id, time)
        db.session.add(q)
        db.session.commit()
        cur_order_id += 1
        cur_order = []
        order_sum = 0
        temp = cur_cafe
        cur_cafe = 0
        order_time = 0

    return render_template('order_accepted.html', o_num=q.queue_index, cafe=db.session.query(Cafes).filter_by(cafe_id=temp)[0].cafe_name )


@app.route("/my_order", methods=['GET', 'POST'])
def my_order():
    global cur_order
    global cur_cafe
    global order_sum
    global min_order_sum
    global order_time

    if request.method == 'POST':
        cur_cafe = 0
        cur_order = []
        order_sum = 0
        order_time = 0

        return render_template('my_order.html', order=cur_order, dishes=db.session.query(Dishes).all(),
                        clean=CleanOrder(request.form), pay=Purchase(request.form), order_sum=order_sum,
                               min=min_order_sum)
    cafes = db.session.query(Cafes).all()
    qu = db.session.query(Queue).all()
    names = [(cafe.cafe_id, cafe.cafe_name) for cafe in cafes]
    ques = [(q.queue_index, q.order_time, q.orders.cafe_id) for q in qu]
    left = 0
    for ordr in ques:
        if cur_cafe == ordr[2]:
            left += ordr[1]

    return render_template('my_order.html', order=cur_order, dishes=db.session.query(Dishes).all(),
                           clean=CleanOrder(request.form), pay=Purchase(request.form), order_sum=order_sum,
                               min=min_order_sum, left=left+order_time)


@app.route('/dish', methods=['GET', 'POST'])
def dish():
    form_dish = DishAddForm(request.form)

    if request.method == 'POST':
        cafe_id = request.form['cafe_id']
        name = request.form['dish_name']
        price = request.form['dish_price']
        desc = request.form['dish_describe']
        time = request.form['dish_avg_time']
        try:
            dish = Dishes(name, cafe_id, price, desc, time)
            db.session.add(dish)
            db.session.commit()

            return "Dish added {}".format(dish.dish_id)

        except Exception as e:
            return str(e)

    return render_template('dish.html', form_dish=form_dish)


@app.route('/cafe', methods=['GET', 'POST'])
def cafe():
    form = CafeAddForm(request.form)

    if request.method == 'POST':
        name = request.form['cafe_name']
        pop = request.form['cafe_popularity']
        try:
            c = Cafes(name, pop)
            db.session.add(c)
            db.session.commit()

            return "Cafe added {}".format(c.cafe_id)

        except Exception as e:
            return str(e)

    return render_template('cafe.html', form=form)


@app.route('/payment', methods=['GET', 'POST'])
def pay():
    return render_template('payment.html', canc=Cancel(request.form), push=PushOrder(request.form))


if __name__ == '__main__':
    app.run()
