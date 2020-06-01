from flask import Flask, render_template,redirect, request, url_for
from distionaries import user_dict, book_dict

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<action>/')
def api_action(action):
    if action == "book":
        return render_template('book.html', book=book_dict)
    elif action == "user":
        return render_template('user.html', user=user_dict)
    elif action == "all":
        return render_template('show.html', book=book_dict, user=user_dict)
    else:
        return render_template('404.html')


@app.route('/book', methods=['GET', 'POST'] )
def api_book():
    if request.method == "POST":
        book_dict['name'] = request.form['name']
        book_dict['url'] = request.form['url']
        book_dict['create_time'] = request.form['create_time']
        book_dict['author'] = request.form['author']
        return redirect(url_for('api_action', action='all'))
    else:
        return redirect(url_for('api_action', action='book'))


@app.route('/user', methods=['GET', 'POST'])
def api_user():
    if request.method == "POST":
        user_dict['fullname'] = request.form['fname']
        user_dict['email'] = request.form['email']
        user_dict['registration'] = request.form['rgstr']
        user_dict['id'] = request.form['id']
        user_dict['login'] = request.form['login']
        user_dict['book_amount'] = request.form['amount']
        return redirect(url_for('api_action', action='all'))
    else:
        return redirect(url_for('api_action', action='user'))


@app.errorhandler(404)
def page404(error):
    return render_template("404.html")


if __name__ == '__main__':
    app.run()
