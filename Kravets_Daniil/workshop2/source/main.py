from flask import Flask, render_template, request, redirect, url_for
from forms import SongForm, OrderForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "songs":
        return render_template("songs.html", songs=songs_dict)
    elif action == "orders":
        return render_template("orders.html", orders=orders_dict)
    elif action == "all":
        return render_template("all.html", songs=songs_dict, orders=orders_dict)
    else:
        return render_template("404.html", action_value=action)

@app.route('/api/songs', methods=['GET', 'POST'])
def api_songs():
    form = SongForm()
    if form.is_submitted():
        result = request.form
        songs_dict['song_name'] = result['song_name']
        songs_dict['artist'] = result['artist']
        songs_dict['date_of_release'] = result['date_of_release']
        return redirect(url_for('apiget', action="all"))
    return render_template('songs.html', form=form)

@app.route('/api/orders', methods=['GET', 'POST'])
def api_orders():
    form = OrderForm()
    if form.is_submitted():
        result = request.form
        orders_dict['id'] = result['id']
        orders_dict['order_text'] = result['order_text']
        return redirect(url_for('apiget', action="all"))
    return render_template('orders.html', form=form)

if __name__ == '__main__':
    songs_dict = {'song_name': 'Diver',
                  'artist': 'NICO Touches the Walls',
                  'date_of_release': '21.08.25'}
    orders_dict = {'id': '1',
                   'order_text': 'Happy birthday to you!'}
    app.run()