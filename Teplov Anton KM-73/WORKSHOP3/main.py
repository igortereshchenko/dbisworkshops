from flask import Flask, render_template, request, redirect, url_for
from forms import Manga_Form, Anime_Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "manga":
        return render_template("manga.html", manga=manga_dict)
    elif action == "anime.html":
        return render_template("anime.html", anime=anime_dict)
    elif action == "toghether":
        return render_template("toghether.html", manga=manga_dict, anime=anime_dict)
    else:
        return render_template("404.html", action_value=action)

@app.route('/api/manga', methods=['GET', 'POST'])
def api_manga():
    form = Manga_Form()
    if form.is_submitted():
        result = request.form
        manga_dict['manga_name'] = result['manga_name']
        manga_dict['author'] = result['author']
        manga_dict['year'] = result['year']
        manga_dict['No_Toms'] = result['No_Toms']
        return redirect(url_for('apiget', action="toghether"))
    return render_template('manga.html', form=form)

@app.route('/api/anime', methods=['GET', 'POST'])
def api_anime():
    form = Anime_Form()
    if form.is_submitted():
        result = request.form
        anime_dict['anime_name'] = result['anime_name']
        anime_dict['date'] = result['date']
        anime_dict['No_series'] = result['No_series']
        anime_dict['genre'] = result['genre']
        return redirect(url_for('apiget', action="toghether"))
    return render_template('anime.html', form=form)

if __name__ == '__main__':
    manga_dict = {'manga_name': 'Death Note',
                  'author': 'Tsugumi Ohba',
                    'year': '2002',
                    'No_Toms': '48'}
    anime_dict = {'anime_name': 'Your name',
                   'date': 're',
                    'No_series': '1',
                    'genre': 'romantic'}
    app.run()