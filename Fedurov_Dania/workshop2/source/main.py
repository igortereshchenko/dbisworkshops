from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def hello():
  return (
    {
      "uri": "/",
      "sub_uri":{
            "all":"/api/all",
            "predictions":"/api/prediction",   
            "users":"/api/user",  
          }
    }
  )


@app.route('/api/<action>', methods = [ 'GET'])
def api(action):

   if action == "user":
      return render_template("user.html",user=user_dictionary)

   elif action == "prediction":
      return render_template("prediction.html", prediction=prediction_dictionary)

   elif action == "all":
      return render_template("all.html", user=user_dictionary, prediction=prediction_dictionary)

   else:
      return render_template("404.html", action_value=action)

@app.route('/api/user/submit', methods = ['POST'])
def user_submit():
    if(request.method == 'POST'):
        return str(request.form['users_id'])+"<br>"+str(request.form['first_name'])+"<br>"+str(request.form['age'])+"<br>"+str(request.form['mail'])

@app.route('/api/prediction/submit', methods = ['POST'])
def tour_submit():
    if(request.method == 'POST'):
        return str(request.form['pred_id'])+"<br>"+str(request.form['pred_name'])+"<br>"+str(request.form['pred_date'])


if __name__ == '__main__':

   user_dictionary = {
   			"user_id": 1,
            "user_name":"Dania",
            "user_age": 20,
            "user_mail": 'Dania_fedyrov@gmail.com',
          }

   prediction_dictionary = {
   		   "pred_id" : 1,
           "prediction_name": "today all will be fine!",
           "date": '10072020',
         }

   app.run(port = 5001, debug = True)