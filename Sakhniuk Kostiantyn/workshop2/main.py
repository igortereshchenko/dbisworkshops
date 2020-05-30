from flask import Flask, render_template, request, redirect, url_for
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '5930142'

product_dict = {'product_name': 'Intel Core i9-9900K',
            'type': 'processor',
            'vendor': 'Bob',
            'cost': 15000}

vendor_dict = {'vendor_name': 'Bob',
            'products': 'Intel Core i9-9900K,Intel Core i9-9900K',
            'link': 'none'
             }

@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "product":
        return render_template("product.html", product=product_dict)
    elif action == "vendor":
        return render_template("vendor.html", vendor=vendor_dict)
    elif action == "all":
        return render_template("all.html", product=product_dict, vendor=vendor_dict)
    else:
        return render_template("404.html", action_value=action)

@app.route('/api/product', methods=['GET', 'POST'])
def api_product():
    form = ProductForm()
    if form.is_submitted():
        result = request.form
        product_dict['product_name'] = result['product_name']
        product_dict['type'] = result['type']
        product_dict['vendor'] = result['vendor']
        product_dict['cost'] = result['cost']
        return redirect(url_for('apiget', action="all"))
    return render_template('product.html', form=form)

@app.route('/api/vendor', methods=['GET', 'POST'])
def api_vendor():
    form = VendorForm()
    if form.is_submitted():
        result = request.form
        vendor_dict['vendor_name'] = result['vendor_name']
        vendor_dict['products'] = result['products']
        vendor_dict['link'] = result['link']
        return redirect(url_for('apiget', action="all"))
    return render_template('vendor.html', form=form)


if __name__ == '__main__':
    app.run()