from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):

   if action == "user":
      return render_template("user.html",user=user_dictionary)

   elif action == "order":
      return render_template("order.html", order=order_dictionary)

   elif action == "all":
      return render_template("all.html", user=user_dictionary, order=order_dictionary)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():


   # <button type="submit" form="form_user" name="action" value="user_update">Submit</button>
   # send name="action" and value="user_update" to POST

    if request.form["action"] == "user_update":

        user_dictionary["user_name"] = request.form["name"]
        user_dictionary["user_email"] = request.form["email"]
        user_dictionary["user_password"] = request.form["password"]

    elif request.form["action"] == "order_update":
        order_dictionary["order_date"] = request.form["date"]
        order_dictionary["order_time"] = request.form["time"]
        order_dictionary["num_person"] = request.form["number_of_person"]
        order_dictionary["order_name"] = request.form["person_name"]

    return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':

   user_dictionary = {
            "user_name": "Jane Ostine",
            "user_email": "test1@gmail.com",
            "user_password": "1234"
          }

   order_dictionary = {
           "order_date": "2020-05-20",
           "order_time": "9-00",
           "num_person": 5,
            "order_name": "Jane Ostine"

         }

   app.run()