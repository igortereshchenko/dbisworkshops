from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):
    true_values = ["user", "info", "all"]
    if action == "user":
        return render_template("user.html",user=user_dictionary)

    elif action == "info":
        return render_template("info.html", info=info_dictionary)

    elif action == "all":
        return render_template("all.html", user=user_dictionary, info=info_dictionary)

    else:
        return render_template("404.html", action_value=action, true_v=true_values)


@app.route('/api', methods=['POST'])
def apipost():

   if request.form["action"] == "user_update":

      user_dictionary["login"] = request.form["log"]
      user_dictionary["PASS"] = request.form["PAS"]
      user_dictionary["NICKNAME"] = request.form["NICK"]
      user_dictionary["first_name"] = request.form["first"]
      user_dictionary["FACULTY_NAME"] = request.form["FACULTY"]
      user_dictionary["COURSE_NUMBER"] = request.form["COURSE"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "info_update":

      info_dictionary["NICKNAME"] = request.form["NICK"]
      info_dictionary["LECTION_NAME"] = request.form["LECTION"]
      info_dictionary["RESOURCE_NAME"] = request.form["RESOURCE"]
      info_dictionary["INFORMATION_LINK"] = request.form["INFORMATION"]
      info_dictionary["DATE"] = request.form["DATE"]

      return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':
    user_dictionary = {
       "login": "kiss_LA_ya",
        "PASS": "Nikusya",
        "NICKNAME": "kiss_kiss",
        "first_name": "Nika",
        "FACULTY_NAME": "Applied mathematics",
        "COURSE_NUMBER": "3"
         }


    info_dictionary = {
        "NICKNAME": "Artem",
        "LECTION_NAME": "Programming on Python",
        "RESOURCE_NAME": "www.studpedia.ua",
        "INFORMATION_LINK": "https://telegra.ph/Programming-on-Python",
        "DATE": "2005/05/03"
    }
    app.run()
