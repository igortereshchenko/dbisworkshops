from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/api/<action>', methods = ['GET'])
def parameter(action):

    if action == 'client':
        return render_template('client.html', client = client)

    elif action == 'restaurant':
        return render_template('restaurant.html', restaurant = restaurant)

    elif action == 'all':
        return render_template('all.html', restaurant = restaurant, client = client)

    else:
        return render_template('404.html', action = action)



@app.route('/api', methods = ['POST'])
def post():

    if request.form['action'] == 'client_update':

        client['name'] = request.form["name"]
        client['email'] = request.form["email"]
        client['cl_phone'] = request.form["cl_phone"]
        return redirect(url_for('parameter', action="all"))

    if request.form['action'] == 'restaurant_update':

        restaurant['title'] = request.form["title"]
        restaurant['address'] = request.form["address"]
        restaurant['re_phone'] = request.form["re_phone"]
        return redirect(url_for('parameter', action="all"))



if __name__ == '__main__':

    client = {
        'name': 'random_name',
        'email': 'random_mail',
        'cl_phone': 'random_phone'
    }

    restaurant = {
        'title': 'random_title',
        'address': 'random_address',
        're_phone': 'random_phone',
    }

    app.run(debug = True)