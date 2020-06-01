from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'The main page. Be calm!'

@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):

   if action == "program":
      return render_template("program.html", program=program_dictionaty)

   elif action == "developer":
      return render_template("developer.html", developer=developer_dictionary)

   elif action == "all":
      return render_template("all.html", program=program_dictionaty, developer=developer_dictionary)

   else:
      return render_template("404.html", action_value=action, correct_pages=correct_pages, correct_pages_len=len(correct_pages))


@app.route('/api', methods=['POST'])
def apipost():

   if request.form["action"] == "user_update":

      developer_dictionary["developer_name"] = request.form["first_name"]
      developer_dictionary["developer_age"] = request.form["age"]

      return redirect(url_for('apiget', action="all"))



if __name__ == '__main__':

   correct_pages = ['car', 'developer']

   program_dictionaty = {
            "program_name":"Skype",
            "program_language": "C++",
          }

   developer_dictionary = {
           "developer_name": "Mike",
           "developer_age": 20,
           "developer_stage": "Junior"
         }

   # app.run(debug=True)
   app.run()