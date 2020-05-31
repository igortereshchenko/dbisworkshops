from flask import Flask, render_template, request, abort,  redirect, url_for
app = Flask(__name__)


@app.route('/api/<action>', methods = ['GET'])
def apiget(action):
    if action == "user":

        return render_template("user.html", user=user_dictionary)

    elif action == "dish":
        return render_template("dish.html", dish=dish_dictionary)

    elif action == "all":
        return render_template("all.html", user=user_dictionary, dish=dish_dictionary)

    else:
        return render_template("404.html", action_value=action, user=user_dictionary, dish=dish_dictionary)


#dynamic rout
@app.route('/api', methods=['POST'])
def apipost():


   if request.form["action"] == "user_update":

      user_dictionary["user_name"] = request.form["name"]
      user_dictionary["user_email"] = request.form["email"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "dish_update":

      dish_dictionary["dish_id"] = request.form["id"]
      dish_dictionary["dish_name"] = request.form["name"]
      dish_dictionary["dish_category"] = request.form["category"]

      return redirect(url_for("apiget", action="all"))




if __name__ == '__main__':
    user_dictionary = {
        "user_name": "Hanna",
        "user_email": "user@gmail.com",
    }

    dish_dictionary = {
        "dish_id": 5,
        "dish_name": "Soup",
        "dish_category": "First course"
    }

    app.run(debug=True)