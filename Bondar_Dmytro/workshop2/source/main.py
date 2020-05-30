from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)



@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "event":
        return render_template("event.html", event=event_dict)
    elif action == "user":
        return render_template("user.html", user=user_dict)

    elif action == "all":
        return render_template("all.html", event=event_dict,
                               user=user_dict)
    else:
        return render_template("404.html", action_value=action)
    
      
@app.route('/api', methods=['POST'])
def apipost():

   if request.form["action"] == "user_update":
       
      user_dict["user_name"] = request.form["name"]
      user_dict["user_id"] = request.form["id"]
      
      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "event_update":
       
      event_dict["event_name"] = request.form["name"]
      event_dict["event_date"] = request.form["date"]
      event_dict["event_time"] = request.form["time"]
      
      return redirect(url_for('apiget', action="all"))   
    
    
    
if __name__ == '__main__':
    event_dict = {'event_name': 'Para',
                'event_date': '11/22/63',
                'event_time': '4:20' }
    user_dict = {'user_name': 'Dimas',
                 'user_id': 1}
    app.run()