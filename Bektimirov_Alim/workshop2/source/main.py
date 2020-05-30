from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/')
def hello():
    # return render_template("all.html", director=director_dictionary, film=film_dictionary)
    return 'Hello  world!'
@app.route('/server/api/<action>', methods = [ 'GET'])
def apiget(action):

   if action == "director":
      return render_template("director.html",director=director_dictionary)

   elif action == "film":
      return render_template("film.html", film=film_dictionary)

   elif action == "all":
      return render_template("all.html", director=director_dictionary, film=film_dictionary)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():



   if request.form["action"] == "director_update":

      director_dictionary["director_name"] = request.form["first_name"]
      director_dictionary["director_age"] = request.form["age"]
      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "film_update":

      film_dictionary["film_title"] = request.form["title"]
      film_dictionary["film_genre"] = request.form["genre"]
      film_dictionary["film_year"] = request.form["year"]
      return redirect(url_for('apiget', action="all"))


if __name__ == '__main__':

   director_dictionary = {
            "director_name":"Christopher Nolan",
            "director_age": 49,
          }

   film_dictionary = {
           "film_title": "Interstellar",
           "film_genre": "Sci-Fi",
           "film_year": 2014
         }

   app.run()