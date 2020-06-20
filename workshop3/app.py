from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "info":
        return render_template("insured_person_info.html", info=a_insured)
    elif action == "insurer":
        return render_template("insurer.html", insurer=a_insurer)

    elif action == "all":
        return render_template("all.html", info=a_insured, insurer=a_insurer)

    else:
        return render_template("404.html", info=a_insured, insurer=a_insurer, action_value=action)

@app.route('/api/', methods=['POST'])
def apipost(action):
    if request.form["action"] == 'info_update':
        a_insured["person_id"] = request.form["id"]
        a_insured["person_firststname"] = request.form["firststname"]
        a_insured["person_lastname"] = request.form["lastname"]
        a_insured["person_d_birth"] = request.form["d_birth"]
        a_insured["person_passport"] = request.form["passport"]
        a_insured["person_itin"] = request.form["itin"]
        a_insured["user_cityzenship"] = request.form["cityzenship"]

        return redirect(url_for("apiget", action="all"))

    if request.form["action"] == 'insurer_update':
        a_insurer["insurer_id"] = request.form["id"]
        a_insurer["insurer_name"] = request.form["name"]
        a_insurer["insurer_password"] = request.form["password"]
        a_insurer["insurer_email"] = request.form["email"]


        return redirect(url_for("apiget", action="all"))


if __name__ == '__main__':

    a_insured = {
        "person_id": 1,
        "person_firstname": "Elena",
        "person_lastname": "Komarova",
        "person_d_birth": 16072000,
        "person_passport": 433444,
        "person_itin": 23344455,
        "person_cityzenship": "Ukraine",

    }

    a_insurer= {
        "insurer_id": 1,
        "insurer_name": "Lena",
        "insurer_password": 1234,
        "insurer_email": "lena@gmail.com",


    }

    app.run(debug=True)