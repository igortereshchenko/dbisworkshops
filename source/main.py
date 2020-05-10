from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY']= '{{thing.waste_sum}}'


@app.route('/')
def start():
    return 'hi there'

@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):
    if action == "waste":
        return render_template("waste.html", waste = waste_dictionary)
    elif action == "category":
        return render_template("category.html", category = category_dictionary)
    elif action == "all":
        return render_template("all.html", waste = waste_dictionary, category = category_dictionary)
    else:
        return render_template("404.html")
@app.route('/api', methods=['POST'])
def apipost():
    if request.form["action"] == "waste_update":
        waste_dictionary[0]['category_name'] = request.form["name"]
        waste_dictionary[0]["waste_sum"] = request.form["sum"]
        waste_dictionary[0]["waste_time"] = request.form["time"]

        return redirect(url_for('apiget', action="all"))
    if request.form["action"] == "category_update":
        category_dictionary[0]['category_name'] = request.form["name"]
        category_dictionary[0]["limit"] = request.form["limit"]

        return redirect(url_for('apiget', action="all"))

if __name__ == '__main__':

   waste_dictionary = [{
            'category_name':"Їжа",
            "waste_sum": 20,
            "waste_time": 123,
   } ]

   category_dictionary = [{
           "category_name": "Їжа",
           "limit": 600,
         }]

   app.run()