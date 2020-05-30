from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "user":
        return render_template("user.html", user=user_dictionary)

    elif action == "tour":
        return render_template("tour.html", tour=tour_dictionary)

    elif action == "all":
        return render_template("all.html", user=user_dictionary, tour=tour_dictionary)

    else:
        return render_template("404.html", action_value=action)


@app.route('/api/user/submit', methods=['POST'])
def user_submit():
    if (request.method == 'POST'):
        return str(request.form['first_name']) + " " + str(request.form['age'])


@app.route('/api/tour/submit', methods=['POST'])
def tour_submit():
    if (request.method == 'POST'):
        return str(request.form['country']) + " " + str(request.form['price'])


if __name__ == '__main__':
    user_dictionary = {
        "user_name": "Bob",
        "user_age": 20,
    }

    tour_dictionary = {
        "tour_country": "France",
        "tour_price": 100,
    }

    app.run()
