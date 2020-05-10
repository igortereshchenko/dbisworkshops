from flask import Flask, request, render_template


app = Flask(__name__)
book_name = 'book'
customer_name = 'customer'
book = {
  "Name": "Metro2033",
  "Author": "Dmitriy Gluchovski",
  "Genre": "Fantasy",
  "Price": "$12",
  "Short description": "Book about how people were living in metro after global war",
  "edition": "Edition ACT, Moscow",
  "number of purchases": "100500"
}
customer = {
  "First name": "Mike",
  "Second name": "Mosby",
  "E-mail": "mikemosby@gmail.com",
  "Login": "max_mike",
  "Password": "just_lina",
    }


@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/info/')
def info():
    return render_template('info.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/sign_in/')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign_up/')
def sign_up():
    return render_template('sign_up.html')


@app.route('/api/<action>', methods=['POST', 'GET'])
def task(action):
    if action == book_name:
        return render_template('book.html', book=book)
    elif action == customer_name:
        return render_template('customer.html', customer=customer)
    elif action == "all":
        return render_template('all.html', book=book, customer=customer)
    else:
        return render_template('404.html',  action=action, book_name=book_name, customer_name=customer_name), 404


@app.route('/api/Metro2033/submit', methods=['POST', 'GET'])
def book_form():
    global book
    if request.method == "POST":
        book["Name"] = request.form['name']
        book["Author"] = request.form['author']
        book["Genre"] = request.form['genre']
        book["Price"] = request.form['price']
        book["Short description"] = request.form['descr']
        book["edition"] = request.form['edition']
        book["number of purchases"] = request.form['number']
        return render_template("all.html", book=book, customer=customer)
    else:
        return render_template("book.html", book=book)


@app.route('/api/Mike/submit', methods=['POST', 'GET'])
def customer_form():
    global customer
    if request.method == "POST":
        customer["First name"] = request.form['first']
        customer["Second name"] = request.form['second']
        customer["E-mail"] = request.form['email']
        customer["Login"] = request.form['login']
        customer["Password"] = request.form['pass']
        return render_template("all.html", book=book, customer=customer)
    else:
        return render_template("customer.html", customer=customer)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', book_name=book_name, customer_name=customer_name), 404


if __name__ == "__main__":
    app.run(debug=True)
