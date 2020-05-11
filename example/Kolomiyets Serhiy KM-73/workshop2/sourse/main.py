from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):
    if action == "user":
      return render_template("user.html",user=user_dictionary)

    elif action == "instrum":
      return render_template("instrument.html", instrum=instrum_dictionary)

    elif action == "all":
      return render_template("all.html", user=user_dictionary, instrum=instrum_dictionary)
    else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():

   if request.form["action"] == "user_update":

      user_dictionary["user_name"] = request.form["first_name"]
      user_dictionary["user_phone"] = request.form["phone"]

      return redirect(url_for('apiget', action="all"))
   if request.form["action"] == "instrum_update":

      instrum_dictionary["instrum_type"] = request.form["type"]
      instrum_dictionary["instrum_model"] = request.form["model"]
      instrum_dictionary["instrum_country"] = request.form["country"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "update_user":
      return redirect(url_for('apiget', action="user"))
   if request.form["action"] == "update_instrum":
       return redirect(url_for('apiget', action="instrum"))



if __name__ == '__main__':

   user_dictionary = {
            "user_name":"Andiy",
            "user_phone": 78678687,
          }

   instrum_dictionary = {
           "instrum_type": "Guitar",
           "instrum_model": "FA-125",
           "instrum_country":"USA"
         }

   app.run()