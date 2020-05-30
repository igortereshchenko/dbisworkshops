from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_dict = {
    "Name": "Kostiantyn",
    "Id": "5"
}

user_resources = {
    "Category": "business",
    "Location": "Germany"
}


@app.route('/<action>', methods=['GET'])
def get_info(action):
    if request.method == 'GET':
        if action == "user_dict":
            return render_template('User_dict.html', user_dict=user_dict)
        elif action == "user_resources":
            return render_template("User_resources.html", user_resources=user_resources)
        elif action == "all":
            return render_template("All.html", users=user_dict, resources=user_resources)
        else:
            return render_template("Error.html")


@app.route('/<action>/add', methods=['POST'])
def post(action):
    if action == 'user_dict':
        if request.form['action'] == "new_user":
            user_dict["Name"] = request.form['name']
            user_dict["Id"] = request.form['id']
            return redirect(url_for('get_info', action="all"))
    if action == 'user_resources':
        if request.form['action'] == "new_user":
            user_resources["Category"] = request.form['category']
            user_resources["Location"] = request.form['location']
            return redirect(url_for('get_info', action="all"))


app.run()