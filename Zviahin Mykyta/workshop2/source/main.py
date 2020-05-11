from flask import Flask, render_template, request, redirect, url_for
from form import UserForm, productForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'keyzviahin'


@app.route('/api/<action>', methods=['GET'])
def get_template(action):
    if action == 'user':
        return render_template('user.html', user=user_dict)
    elif action == 'product':
        return render_template('product.html', product=product_dict)
    elif action == 'all':
        return render_template('all.html', user=user_dict, product=product_dict)
    else:
        return render_template('404.html', action_value=action)


@app.route('/api/user', methods=['GET', 'POST'])
def api_user():
    form = UserForm()
    if form.is_submitted():
        result = request.form
        user_dict['id'] = result['user_id']
        user_dict['firstName'] = result['user_first_name']
        user_dict['lastName'] = result['user_last_name']
        user_dict['email'] = result['user_email']
        return redirect(url_for('get_template', action="all"))
    return render_template('user.html', form=form)


@app.route('/api/product', methods=['GET', 'POST'])
def api_product():
    form = productForm()
    if form.is_submitted():
        result = request.form
        product_dict['id'] = result['product_id']
        product_dict['name'] = result['product_name']
        product_dict['userId'] = result['product_user_id']
        return redirect(url_for('get_template', action="all"))
    return render_template('product.html', form=form)


if __name__ == '__main__':
    user_dict = {
        'id': '2203',
        'firstName': 'Nikita',
        'lastName': 'Zviahin',
        'email': 'blabla@yahoo.com'
    }
    product_dict = {
        'id': 'someproductid',
        'name': 'someproduct',
        'userId': 'someid',
    }

    app.run()
