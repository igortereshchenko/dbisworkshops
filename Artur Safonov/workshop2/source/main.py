from flask import Flask, render_template, request
from forms import UserForm, CardForm


data = {}
data['user'] = {
    "name": "Bob",
    "surname": "Bobenko",
    "middle_name": "Bobovich",
    "phone": "+380501234567",
    "email": "bob.bobenko@gmail.com"}
data['card'] = {
    "number": "5160123456789010",
    "name": "Bob Bobenko",
    "date": "11.05.2024",
    "cvv": "123"}


app = Flask(__name__)
app.config['SECRET_KEY'] = 'q'

@app.route('/api/<action>', methods=['GET', 'POST'])
def index(action):
    if action == 'user':
        form = UserForm()
        if form.is_submitted():
            result = request.form
            addUserToDict(result)
        return render_template('user.html', form=form)
    elif action == 'card':
        form = CardForm()
        if form.is_submitted():
            result = request.form
            addCardToDict(result)
        return render_template('card.html', form=form)
    elif action == 'all':
        return render_template('all.html', users=data['user'], cards=data['card'])
    else:
        return render_template('404.html', entity=action), 404

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404


def addUserToDict(user):
    data['user']['name'] = user['name']
    data['user']['surname'] = user['surname']
    data['user']['middle_name'] = user['middle_name']
    data['user']['phone'] = user['phone']
    data['user']['email'] = user['email']


def addCardToDict(card):
    data['card']['number'] = card['number']
    data['card']['name'] = card['name']
    data['card']['date'] = card['date']
    data['card']['cvv'] = card['cvv']



if __name__ == '__main__':
    app.run(debug=True)