from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "user":
        return render_template("user.html", user=user_d)

    elif action == "studio":
        return render_template("studio.html", studio=studio_d)

    elif action == "all":
        return render_template("all.html", user=user_d, studio=studio_d)

    else:
        return render_template("404.html", user=user_d, studio=studio_d, action_value=action)

@app.route('/api/', methods=['POST'])
def apipost(action):
    if request.form["action"] == '"user_apdate':
        user_d["user_id"] = request.form["id"]
        user_d["user_name"] = request.form["name"]
        user_d["user_email"] = request.form["email"]

        return redirect(url_for("apiget", action="all"))

    if request.form["action"] == '"studio_apdate':
        studio_d["studio_id"] = request.form["id"]
        studio_d["studio_name"] = request.form["st_name"]
        studio_d["studio_email"] = request.form["st_email"]
        studio_d["studio_number"] = request.form["st_number"]
        studio_d["studio_address"] = request.form["st_address"]

        return redirect(url_for("apiget", action="all"))


if __name__ == '__main__':

    user_d = {
        "user_id": 1,
        "user_name": "Ann",
        "user_email": "ann@gmail.com"
    }

    studio_d = {
        "studio_id": 3,
        "studio_name": "Luckoutclub",
        "studio_email": "luckout@gmail.com",
        "studio_number": "099 123 1234",
        "studio_address": "Heroiv dnipra 1"
    }

    app.run(debug=True)
