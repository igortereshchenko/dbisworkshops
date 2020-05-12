from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

customer_dictionary = {
    "customer_name": "Nikolas Barkeeper",
    "customer_age": 20,
}

product_dictionary = {
    "product_title": "Shaker",
    "product_description": "shake your cocktails",
    "product_amount": 2
}


@app.route('/')
def hello():
    return render_template("home.html")


@app.route('/server/api/<action>', methods=['GET'])
def apiget(action):
    if action == "customer":
        return render_template("customer.html", customer=customer_dictionary)

    elif action == "product":
        return render_template("product.html", product=product_dictionary)

    elif action == "all":
        return render_template("all.html", customer=customer_dictionary, product=product_dictionary)

    else:
        return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():
    if request.form["action"] == "redirect_all":
        return redirect(url_for('apiget', action="all"))

    if request.form["action"] == "redirect_customer":
        return redirect(url_for('apiget', action="customer"))

    if request.form["action"] == "redirect_product":
        return redirect(url_for('apiget', action="product"))

    if request.form["action"] == "customer_update":
        customer_dictionary["customer_name"] = request.form["name"]
        customer_dictionary["customer_age"] = request.form["age"]
        return redirect(url_for('apiget', action="all"))

    if request.form["action"] == "product_update":
        product_dictionary["product_title"] = request.form["title"]
        product_dictionary["product_description"] = request.form["description"]
        product_dictionary["product_amount"] = request.form["amount"]
        return redirect(url_for('apiget', action="all"))


if __name__ == '__main__':
    app.run()
