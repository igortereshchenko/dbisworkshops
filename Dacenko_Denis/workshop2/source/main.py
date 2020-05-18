from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_dict = {
    "user_name": "Neron Caesar",
    "user_age": 40,
}

card_dict = {
    "card_name": "Sorin Markov",
    "card_set": "m15",
    "card_price": 111,
}

@app.route('/')
def hello():
    return 'Hello  world!'


@app.route('/server/api/<action>', methods = ['GET'])
def apiget(action):

   if action == "user":
      return render_template("user.html",user=user_dict)

   elif action == "card":
      return render_template("card.html", card=card_dict)

   elif action == "all":
      return render_template("all.html", user=user_dict, card=card_dict)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():

   if request.form["action"] == "user_update":

      user_dict["user_name"] = request.form["first_name"]
      user_dict["user_age"] = request.form["age"]
      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "card_update":

      card_dict["card_name"] = request.form["name"]
      card_dict["card_set"] = request.form["set"]
      card_dict["card_price"] = request.form["price"]
      return redirect(url_for('apiget', action="all"))


if __name__ == '__main__':



   app.run()