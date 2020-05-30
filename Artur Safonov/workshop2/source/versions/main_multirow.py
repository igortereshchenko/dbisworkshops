from flask import Flask, render_template, request
from forms import UserForm, CardForm
import json


try:
    with open('data.txt') as json_file:
        data = json.load(json_file)
except:
    data = {}
    data['user'] = []
    data['card'] = []
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


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
        return render_template('all_json.html', users=data['user'], cards=data['card'])
    else:
        return render_template('404.html', entity=action), 404

@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html'), 404


def addUserToDict(user):
    for u in data['user']:
        if u['phone'] == user['phone']:
            u['name'] = user['name']
            u['surname'] = user['surname']
            u['middle_name'] = user['middle_name']
            u['email'] = user['email']
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
            return 0
    data['user'].append({
        'name' : user['name'],
        'surname' : user['surname'],
        'middle_name' : user['middle_name'],
        'phone' : user['phone'],
        'email' : user['email']
    })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def addCardToDict(card):
    for c in data['card']:
        if c['number'] == card['number']:
            c['name'] = card['name']
            c['date'] = card['date']
            c['cvv'] = card['cvv']
            with open('data.txt', 'w') as outfile:
                json.dump(data, outfile)
            return 0
    data['card'].append({
        'number': card['number'],
        'name': card['name'],
        'date': card['date'],
        'cvv': card['cvv'],
    })
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

if __name__ == '__main__':
    app.run(debug=True)