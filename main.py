from flask import Flask, render_template, request, redirect, url_for
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '6472674'

hike_dict = {'hike_name': 'Mrmaarosy',
            'during': 6,
            'km': 80,
            'complexity': 3,
            'start_date': '14-03-2020',
             'cost': 3000}

user_dict = {'user_name': 'Dima',
            'weight': 70,
            'height': 180,
            'birth_date': '14-05-1999',
            'diseases': 'none',
             }


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "hike":
        return render_template("hike.html", hike=hike_dict)

    elif action == "user":
        return render_template("user.html", user=user_dict)

    elif action == "all":
        return render_template("all.html", hike=hike_dict,
                               user=user_dict)

    else:
        return render_template("404.html", action_value=action)


@app.route('/api/hike', methods=['GET', 'POST'])
def api_hike():
    form = HikeForm()
    if form.is_submitted():
        result = request.form
        hike_dict['during'] = result['during']
        hike_dict['hike_name'] = result['hike_name']
        hike_dict['km'] = result['km']
        hike_dict['complexity'] = result['complexity']
        hike_dict['start_date'] = result['start_date']
        hike_dict['cost'] = result['cost']
        return redirect(url_for('apiget', action="all"))
    return render_template('hike.html', form=form)


@app.route('/api/user', methods=['GET', 'POST'])
def api_user():
    form = UserForm()
    if form.is_submitted():
        result = request.form
        user_dict['user_name'] = result['user_name']
        user_dict['weight'] = result['weight']
        user_dict['height'] = result['height']
        user_dict['birth_date'] = result['birth_date']
        user_dict['diseases'] = result['diseases']
        return redirect(url_for('apiget', action="all"))
    return render_template('user.html', form=form)

if __name__ == '__main__':
    app.run()