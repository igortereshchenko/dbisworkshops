from flask import Flask, render_template 
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def hello():
  return (
    {
      "uri": "/",
      "sub_uri":{
            "alldata":"/api/all",
            "todolist":"/api/todo",   
            "users":"/api/user",  
          }
    }
  )


@app.route('/api/<action>', methods = [ 'GET'])
def api(action):

   if action == "user":
      return render_template("user.html",user=user_dictionary)

   elif action == "todo":
      return render_template("todo.html", todo=todo_dictionary)

   elif action == "all":
      return render_template("all.html", user=user_dictionary, todo=todo_dictionary)

   else:
      return render_template("404.html", action_value=action)

@app.route('/api/user/submit', methods = ['POST'])
def user_submit():
    if(request.method == 'POST'):
        return "<h3>Name:  "+str(request.form['first_name'])+"<br>Age:  "+str(request.form['age'])+"<br>Mail:  "+str(request.form['mail'])+"</h3>"

@app.route('/api/todo/submit', methods = ['POST'])
def tour_submit():
    if(request.method == 'POST'):
        return '<h3>Name:  '+str(request.form['todo_name'])+"<br>Note:  "+str(request.form['description'])+"<br>start time:  "+str(request.form['time_start'])+"<br>end time:  "+str(request.form['time_end'])+"</h3>"

if __name__ == '__main__':

   user_dictionary = {
            "user_name":"Pasha",
            "user_age": 20,
            "user_mail": 'lysyi.pavlos@gmail.com',
          }

   todo_dictionary = {
           "todo_name": "Clean my room",
           "todo_description": 'clean and do the washing up',
           "todo_start_time": '11:30',
           "todo_end_time": '11:45',
         }

   app.run(port = 5001, debug = True)