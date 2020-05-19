from flask import Flask, request, render_template


app = Flask(__name__)
game_name = 'game'
username = 'user'
game = {
  "Title": "Dota2",
  "Genre": "MOBA",
  "Description": "Typical MOBA",
  "Version": "7.26",
  "Number of donwloads": "1005000000"
}
user = {
  "Username":"chichi25",
  "Email":"chichi25@gmail.com",
  "Type":"standart",
  "Favorite genre":"MOBA",
  "Password": "qwerty123"
  }


@app.route('/')
def index():
    return render_template('main_page.html')






@app.route('/sign_in/')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign_up/')
def sign_up():
    return render_template('sign_up.html')


@app.route('/api/<action>', methods=['POST', 'GET'])
def task(action):
    if action == game_name:
        return render_template('game.html',game=game)
    elif action == username:
        return render_template('user.html', user=user)
    elif action == "all":
        return render_template('all.html', game=game, user=user)
    else:
        return render_template('404.html',  action=action, game=game, user=user), 404


@app.route('/api/Dota2/submit', methods=['POST', 'GET'])
def game_form():
    global game
    if request.method == "POST":
        game["Title"] = request.form['title']
        game["Genre"] = request.form['genre']
        game["Version"] = request.form['version']
        game["Description"] = request.form['descr']
        game["Number of downloads"] = request.form['number']
        return render_template("all.html", game=game, user=user)
    else:
        return render_template("game.html", game=game)


@app.route('/api/Mike/submit', methods=['POST', 'GET'])
def user_form():
    global user
    if request.method == "POST":
        user["Username"] = request.form['name']
        user["Email"] = request.form['email']
        user["Type"] = request.form['type']
        user["Favorite genre"] = request.form['genre']
        user["Password"] = request.form['pass']
        return render_template("all.html",game=game, user=user)
    else:
        return render_template("user.html", user=user)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', game_name=game_name, username=username), 404


if __name__ == "__main__":
    app.run(debug=True)
