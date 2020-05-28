from flask import Flask, request, render_template


app = Flask(__name__)
games_name = 'game'
customer_name = 'customer'
games = {
  "Name": "Just a game",
  "Author": "Hobby gorld",
  "Genre": "DnD",
  "Price": "$30",
  "Short description": "Just a game",
  "edition": "Edition 2, Deli",
  "number of purchases": "100000"
}
customer = {
  "First name": "Raw",
  "Second name": "Becone",
  "E-mail": "rwb@gmail.com",
  "Login": "RawRaw",
  "Password": "becone",
    }


@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/info/')
def info():
    return render_template('info.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/sign_in/')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign_up/')
def sign_up():
    return render_template('sign_up.html')


@app.route('/api/<action>', methods=['POST', 'GET'])
def task(action):
    if action == game_name:
        return render_template('game.html', game=game)
    elif action == customer_name:
        return render_template('customer.html', customer=customer)
    elif action == "all":
        return render_template('all.html', game=game, customer=customer)
    else:
        return render_template('404.html',  action=action, game_name=game_name, customer_name=customer_name), 404


@app.route('/api/Metro2033/submit', methods=['POST', 'GET'])
def game_form():
    global game
    if request.method == "POST":
        game["Name"] = request.form['name']
        game["Author"] = request.form['author']
        game["Genre"] = request.form['genre']
        game["Price"] = request.form['price']
        game["Short description"] = request.form['descr']
        game["edition"] = request.form['edition']
        game["number of purchases"] = request.form['number']
        return render_template("all.html", game=game, customer=customer)
    else:
        return render_template("game.html", game=game)


@app.route('/api/Mike/submit', methods=['POST', 'GET'])
def customer_form():
    global customer
    if request.method == "POST":
        customer["First name"] = request.form['first']
        customer["Second name"] = request.form['second']
        customer["E-mail"] = request.form['email']
        customer["Login"] = request.form['login']
        customer["Password"] = request.form['pass']
        return render_template("all.html", game=game, customer=customer)
    else:
        return render_template("customer.html", customer=customer)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', game_name=game_name, customer_name=customer_name), 404


if __name__ == "__main__":
    app.run(debug=True)
