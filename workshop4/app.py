from flask import Flask, render_template, request, redirect, url_for
from forms import *
import datetime
from Models import *

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
app.config['SECRET_KEY'] = '6472674'


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "hike":
        return render_template("hike.html")

    elif action == "user":
        return render_template("user.html")

    elif action == "order":
        return render_template("order.html")

    elif action == "sentence":
        return render_template("sentence.html")

    elif action == "all_hikes":
        return render_template("all.html", select=MasterSQL.Select(Hikes))

    elif action == "all_users":
        return render_template("all.html", select=MasterSQL.Select(Users))

    elif action == "all_orders":
        return render_template("all.html", select=MasterSQL.Select(Orders))

    elif action == "all_sentences":
        return render_template("all.html", select=MasterSQL.Select(Sentences))
    else:
        return render_template("404.html", action_value=action)


@app.route('/api/hike', methods=['GET', 'POST'])
def api_hike():
    form = HikeForm()
    if form.is_submitted():
        result = request.form

        new_row = Hikes(
            hike_name=result["hike_name"],
            duration=result["duration"],
            complexity=result["complexity"],
            length=result["length"],
            price=result["price"])

        MasterSQL.Insert(new_row)
        return redirect(url_for('apiget', action="all_hikes"))
    return render_template('hike.html', form=form)


@app.route('/api/user', methods=['GET', 'POST'])
def api_user():
    form = UserForm()
    if form.is_submitted():
        result = request.form
        date = [int(i) for i in result["birth_date"].split('.')]

        new_row = Users(fio=result["fio"],
                        birth_date=datetime.date(date[0], date[1], date[2]),
                        equipment=result["equipment"],
                        healthy=result["healthy"],
                        height=result["height"],
                        weight=result["weight"])

        MasterSQL.Insert(new_row)
        return redirect(url_for('apiget', action="all_users"))
    return render_template('user.html', form=form)


@app.route('/api/order', methods=['GET', 'POST'])
def api_order():
    form = OrderForm()
    if form.is_submitted():
        result = request.form

        new_row = Orders(
            fk_sentence_id=result["fk_sentence_id"],
            fk_user_id=result["fk_user_id"])

        MasterSQL.Insert(new_row)

        return redirect(url_for('apiget', action="all_orders"))
    return render_template('order.html', form=form)


@app.route('/api/sentence', methods=['GET', 'POST'])
def api_sentence():
    form = SentenceForm()
    if form.is_submitted():
        result = request.form
        date = [int(i) for i in result["start_date"].split('.')]

        new_row = Sentences(
            fk_hike_id=result["fk_hike_id"],
            start_date=datetime.date(date[0], date[1], date[2]))

        MasterSQL.Insert(new_row)
        return redirect(url_for('apiget', action="all_sentences"))
    return render_template('sentence.html', form=form)


if __name__ == '__main__':
    app.run()
