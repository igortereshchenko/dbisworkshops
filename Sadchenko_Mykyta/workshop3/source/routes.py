from flask import (
    Flask, render_template, request, redirect, url_for,
    session
)
from source import app
from .models import User
from config import Config

import json


init_user = User("iamreliableuser", "Composer")


def json_dump_from_dict(db_path, json_name, var):
    with open("{}{}".format(db_path, json_name), 'w') as f:
        json.dump(var, f)

def from_json_to_dict(db_path, file_name):
    with open("{}{}".format(db_path, file_name), 'r') as json_file:
        data = json.load(json_file)
    return data


composers = from_json_to_dict(Config.DATABASE, "composers.json")
songs = from_json_to_dict(Config.DATABASE, "songs.json")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    session['username'] = init_user.username
    session['user_type'] = init_user.user_type

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('user_type', None)

    return redirect(url_for('index'))


@app.route('/api/<action>', methods = ['GET'])
def api_get(action):
    if action == "composer":
        return render_template("composer.html", title="Composer-not-poser", composer=composers)
    elif action == "song":
        return render_template("song.html", title="Song-g-g", song=songs)
    elif action == "all":
        return render_template("all.html", title="its all that i have", composers=composers, songs=songs)
    else:
        return render_template("404.html", title="oops, man", action_value=action)


@app.route('/api/composer/submit', methods=['POST'])
def api_composer_post():
    if request.form["action"] == "composer_update":
        composers["first_name"] = request.form["first_name"]
        composers["last_name"] = request.form["last_name"]
        composers["country"] = request.form["country"]
        composers["city"] = request.form["city"]
        composers["born_at"] = request.form["born_at"]

        json_dump_from_dict(Config.DATABASE, 'composers.json', composers)

        return redirect(url_for('api_get', action="all"))


@app.route('/api/song/submit', methods=['POST'])
def api_songs_post():
    if request.form["action"] == "song_update":
        songs["title"] = request.form["title"]
        songs["lyrics"] = request.form["lyrics"]
        songs["author"] = request.form["author"]
        songs["genre"] = request.form["genre"]
        songs["year"] = request.form["year"]

        json_dump_from_dict(Config.DATABASE, 'songs.json', songs)

        return redirect(url_for('api_get', action="all"))
