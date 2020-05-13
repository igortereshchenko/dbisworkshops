from flask import Flask, render_template, session, redirect, url_for, jsonify

from Kostetskiy_Nazar.workshop2.source.config import SECRET_KEY
from Kostetskiy_Nazar.workshop2.source.models import Posts, Reviews
from Kostetskiy_Nazar.workshop2.source.models.user import User

app = Flask(__name__)
app.secret_key = SECRET_KEY
current_user = User(username='User1', email='user1@email')


posts = Posts()
reviews = Reviews()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sign_in")
def sign_in():
    session['username'] = current_user.username
    session['email'] = current_user.email
    return redirect(url_for("index"))


@app.route('/sign_out')
def sign_out():
    session.pop('username', None)
    session.pop('user_type', None)

    return redirect(url_for('index'))


@app.route("/api/review/submit", methods=['POST'])
def comment_submit():
    # if request.form["review_action"] == "review_update":
    posts.set_data()

    return redirect(url_for('api_get', action="all"))


@app.route("/api/user_posts/submit", methods=['POST'])
def photographer_submit():
    # if request.form["user_posts_action"] == "user_posts_update":
    return redirect(url_for('api_get', action="all"))


@app.route('/api/<action>', methods=["GET"])
def api_get(action):
    if action == "review":
        return jsonify(reviews.data), 200

    elif action == "user_posts":
        return jsonify(posts.data), 200

    elif action == "all":
        return jsonify({'review': reviews.data, 'user_posts': posts.data}), 200

    else:
        return jsonify({'result': False}), 404


if __name__ == "__main__":
    app.run('127.0.0.1', 5555, debug=True)
