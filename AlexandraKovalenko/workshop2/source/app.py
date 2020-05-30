from flask import Flask, render_template, request, abort,  redirect, url_for
app = Flask(__name__)


@app.route('/api/<action>', methods = ['GET'])
def actinfo(action):
    if action == "student":

        return render_template("patient.html", patient=patient)

    elif action == "book":
        return render_template("diagnostic.html", diagnostic=diagnostic)

    elif action == "all":
        return render_template("all.html", patient=patient, diagnostic=diagnostic)

    else:
        return render_template("404.html", action=action, patient=patient, diagnostic=diagnostic)



@app.route('/api', methods=['POST'])
def update():

   if request.form["action"] == "patient_update":

      patient["username"] = request.form["username"]
      patient["id"] = request.form["id"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "diagnostic_update":

      diagnostic["kind"] = request.form["kind"]
      diagnostic["doctor"] = request.form["doctor"]
      diagnostic["diagnostic"] = request.form["diagnostic"]

      return redirect(url_for("actinfo", action="all"))




if __name__ == '__main__':
    diagnostic = {
        "kind": "stomatology",
        "doctor": "stomatolog",
        "year":  "caries"

    }
    patient = {
        "username": "Sasha",
        "id": "10"

    }

    app.run(debug=True)