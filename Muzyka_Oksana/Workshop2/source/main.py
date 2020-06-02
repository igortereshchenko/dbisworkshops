from flask import Flask, render_template



app = Flask(__name__)

@app.route('/api/<action>', methods = ['GET', 'POST'])
def apiget(action):
	if action == 'group':
		return render_template('group.html', group = groups)
	elif action == 'customer':
		return render_template('customer.html', customer = customers)
	elif action == 'all':
		return render_template('all.html', group = groups, customer = customers)
	else:
		return render_template('404.html')

groups =  {
	"Name":"El-7",
	"Level":"Elementary",
	"Timetable":"Пн-Чт(19:35-21:15)",
	"Teachers":"Anna L, Peter",
	"Price":"1800"
	}
customers = {
	"Name":"Бобич Боб Бобович",
	"Age":"18" 
	"Email":"boobb@mail.com",
	"Phone":"0111111111"
	}

if __name__ == '__main__':
	app.run(debug = True)
