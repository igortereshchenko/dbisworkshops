from flask import Flask, request, render_template

app = Flask(__name__)


nutrition_dictionary = {
    "nutr_title": "Big chicken nutrition pack",
    "nutr_brand": "Purina Pro plan",
    "nutr_ingredient": "Chicken",
    "nutr_weight": 10,
    "nutr_price": 400,
    "nutr_description": "This is a food for dogs"
}

customer_dictionary = {
   "cust_name": "Fedor",
   "cust_surname": "Kuprianov",
   "cust_login": "fedyakup",
   "cust_pass": "poc123poc",
   "cust_email": "fedya_kup@gmail.com",
   "cust_adress": "Volgogradska str."
}


@app.route('/')
def main():
     return 'Priv che delaesh'



@app.route('/api/<action>', methods=['GET'])
def apiget(action):
     if action == "nutrition":
         return render_template('nutrition.html', nutrition=nutrition_dictionary)
     elif action == "customer":
         return render_template('customer.html', customer=customer_dictionary)
     elif action == "all":
         return render_template('all.html', nutrition=nutrition_dictionary, customer=customer_dictionary)
     else:
         return render_template('404.html',  action_value=action)


@app.route('/api/nutrition/submit', methods=['POST'])
def nitrition_submit():
     if request.method == "POST":
         nutrition_dictionary["Title"] = request.form['title']
         nutrition_dictionary["Brand"] = request.form['brand']
         nutrition_dictionary["Ingredient"] = request.form['ingredient']
         nutrition_dictionary["Weight"] = request.form['weight']
         nutrition_dictionary["Price"] = request.form['price']
         nutrition_dictionary["Short description"] = request.form['descr']
         return render_template("all.html", nutrition=nutrition_dictionary, customer=customer_dictionary)
     else:
         return render_template("nutrition.html", nutrition=nutrition_dictionary)


@app.route('/api/customer/submit', methods=['POST'])
def customer_submit():
     if request.method == "POST":
         customer_dictionary["Name"] = request.form['name']
         customer_dictionary["Surname"] = request.form['surname']
         customer_dictionary["Login"] = request.form['login']
         customer_dictionary["Password"] = request.form['pass']
         customer_dictionary["E-mail"] = request.form['email']
         customer_dictionary["Adress"] = request.form['adress']
         return render_template("all.html", nutrition=nutrition_dictionary, customer=customer_dictionary)
     else:
         return render_template("customer.html", customer=customer_dictionary)



if __name__ == "__main__":
     app.run(debug=True)