from flask import Flask
from flask import render_template, session, redirect, url_for, request
from Zelenyi_Dmytro.workshop2.source.user import User

import json
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

custom_user = User("Pupsick228", "Photographer")


def from_json_to_dict(file_name):
    with open("database/{}".format(file_name)) as json_file:
        data = json.load(json_file)

    return data


photographers = from_json_to_dict("photographers.json")
comments = from_json_to_dict("comments.json")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    session['username'] = custom_user.login
    session['user_type'] = custom_user.type

    return redirect(url_for("home"))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_type', None)

    return redirect(url_for('home'))


@app.route("/api/comment/submit", methods=['POST'])
def comment_submit():
    if request.form["comment_action"] == "comment_update":
        comments["autor"] = request.form["autor"]
        comments["for_who"] = request.form["photographer"]
        comments["text"] = request.form["comment"]
        comments["stars"] = request.form["stars"]

        with open("database/comments.json", "w") as f:
            json.dump(comments, f)

        return redirect(url_for('api_get', action="all"))


@app.route("/api/photographer/submit", methods=['POST'])
def photographer_submit():
    if request.form["photographer_action"] == "photographer_update":
        photographers["username"] = request.form["username"]
        photographers["rating"] = request.form["rating"]
        photographers["password"] = request.form["password"]
        photographers["name"] = request.form["name"]
        photographers["surname"] = request.form["surname"]
        photographers["email"] = request.form["email"]
        photographers["gender"] = request.form["gender"]
        photographers["about"] = request.form["about"]
        photographers["experience"] = request.form["experience"]
        photographers["region"] = request.form["region"]
        photographers["city"] = request.form["city"]
        photographers["instagram"] = request.form["instagram"]

        with open("database/photographers.json", "w") as f:
            json.dump(photographers, f)

        return redirect(url_for('api_get', action="all"))


@app.route('/api/<action>', methods=["GET"])
def api_get(action):
    if action == "photographer":
        return render_template("photographer.html", photographer=photographers)

    elif action == "comment":
        return render_template("comment.html", comment=comments)

    elif action == "all":
        return render_template("all.html", photographers=photographers, comments=comments)

    else:
        return render_template("404.html", action_value=action, photographers="photographer", comments="comment",
                               all="all")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
