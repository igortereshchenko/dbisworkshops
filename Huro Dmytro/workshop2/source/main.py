from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

cafe_dictionary = {
                "title": "McDonald's",
                "rank": 1
                }

   dish_dictionary = {
           "name": "burger",
       "description": "the tastiest burburger",
       "price": 12
       }

@app.route('/', methods=['GET'])
def start():
    return render_template("all.html", cafe=cafe_dictionary, dish=dish_dictionary)

@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):

   if action == "cafe":
      return render_template("cafe.html", cafe=cafe_dictionary)

   elif action == "dish":
      return render_template("dish.html", dish=dish_dictionary)

   elif action == "all":
      return render_template("all.html", cafe=cafe_dictionary, dish=dish_dictionary)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():

   # <button type="submit" form="form_user" name="action" value="user_update">Submit</button>
   # send name="action" and value="user_update" to POST

    if request.form["action"] == "cafe_update":
        cafe_dictionary["title"] = request.form["title"]
        cafe_dictionary["rank"] = request.form["rank"]

        return redirect(url_for('apiget', action="all"))

    if request.form["action"] == "dish_update":
        dish_dictionary["name"] = request.form["name"]
        dish_dictionary["description"] = request.form["description"]
        dish_dictionary["price"] = request.form["price"]

        return redirect(url_for('apiget', action="all"))


if __name__ == '__main__':
   

app.run()