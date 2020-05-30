from flask import Flask, render_template
#import json


app = Flask(__name__)

@app.route('/api/<action>', methods = ['GET', 'POST'])
def apiget(action):
	if action == 'edition':
		return render_template('editions.html', edition = editions)
	elif action == 'customer': #замовник
		return render_template('customer.html', customer = customers)
	elif action == 'all':
		return render_template('all.html', edition = editions, customer = customers)
	else:
		return render_template('error.html')

editions =  {
	"Category":"Політика",
	"Nane":"Газета по-українськи",
	"Price":"220",
	"Index":"86555"
	}
customers = {
	"Name":"Петреноко Петро Перович",
	"Email":"user@mail.com",
	"Phone":"0111111111"
	}

if __name__ == '__main__':
	app.run(debug = True)