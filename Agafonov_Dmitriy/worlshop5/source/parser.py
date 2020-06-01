import requests

from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    a = str("hello")
    return a

@app.route("/parser", methods = ['GET'])
def hello1():
    response = requests.get("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    resp = response.json()
    print(response.json()[0])

    ccy = ['USD', 'EUR', 'RUR']
    buy_arr = []
    sale_arr = []

    for i in ccy:
        print(i)
        for j in resp:
            if j['ccy'] == i:
                buy_arr.append(j['buy'])
                sale_arr.append(j['sale'])
    return render_template('parsertest.html')



if __name__ == "__main__":
    app.run(debug = True)


