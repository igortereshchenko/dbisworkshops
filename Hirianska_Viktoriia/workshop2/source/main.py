from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):
   

   if action == "user":
      return render_template("user.html",user=user_dictionary)

   elif action == "series":
      return render_template("series.html", series=series_dictionary)

   elif action == "all":
      return render_template("all.html", user=user_dictionary, series=series_dictionary)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():
   

   if request.form["action"] == "user_update":

      user_dictionary["user_name"] = request.form["name"]
      user_dictionary["user_surname"] = request.form["surname"]
      user_dictionary["user_age"] = request.form["age"]

      return redirect(url_for('apiget', action="all"))
   

   if request.form["action"] == "series_update":

      series_dictionary["series_title"] = request.form["title"]
      series_dictionary["series_genre"] = request.form["genre"]
      series_dictionary["series_year"] = request.form["year"]
      series_dictionary["series_country"] = request.form["country"]

      return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':

   user_dictionary = {
            "user_name": "Viktoriia",
            "user_surname": "Hirianska",
            "user_age": 19,
          }

   series_dictionary = {
           "series_title": "Friends",
           "series_genre": "Sitcom",
           "series_year": 1994,
           "series_country": "United States"
         }

   app.run()
