from flask import Flask, render_template, request, abort,  redirect, url_for
app = Flask(__name__)


@app.route('/api/<action>', methods = ['GET'])
def apiget(action):
    if action == "vendor":

        return render_template("vendor.html", vendor=vendor_dictionary)

    elif action == "event":
        return render_template("event.html", event=event_dictionary)

    elif action == "all":
        return render_template("all.html", vendor=vendor_dictionary, event=event_dictionary)

    else:
        return render_template("404.html", action_value=action, vendor=vendor_dictionary, event=event_dictionary)


#dynamic rout
@app.route('/api', methods=['POST'])
def apipost():


   if request.form["action"] == "vendor_update":

      vendor_dictionary["vendor_name"] = request.form["name"]
      vendor_dictionary["vendor_email"] = request.form["email"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "event_update":

      event_dictionary["event_id"] = request.form["id"]
      event_dictionary["event_name"] = request.form["name"]
      event_dictionary["event_category"] = request.form["category"]

      return redirect(url_for("apiget", action="all"))




if __name__ == '__main__':
    vendor_dictionary = {
        "vendor_name": "Coshey Local DIY",
        "vendor_email": "coshey@gmail.com",
    }

    event_dictionary = {
        "event_id": 5,
        "event_name": "Shoegaze Night",
        "event_category": "Shoegaze"
    }

    app.run(debug=True) 