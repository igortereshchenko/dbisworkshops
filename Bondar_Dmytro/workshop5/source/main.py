import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from flask import Flask, render_template, request, redirect, url_for, Response
from classes import *
app = Flask(__name__)






@app.route('/', methods=['GET'])
def redir():
    return redirect(url_for('apiget', action="user"))  
  

@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "event":
        return render_template("event.html", event=event_dict)
    elif action == "user":
        return render_template("user.html", user=user_dict)

    elif action == "all":
        ev_list = Event.event_list(user_dict["user_id"])
        event_list = []
        for row in ev_list:
            event_list.append(row)
        
        return render_template("all.html", event=event_dict,
                               user=user_dict, elist = event_list)
    else:
        return render_template("404.html", action_value=action)
    
      
@app.route('/api', methods=['POST'])
def apipost():
    if request.form["action"] == "user_update":
        try:
            new_user = User()
            new_user.add_user(request.form["name"], request.form["username"], request.form["pass"])
            user_dict["user_name"] = request.form["name"]
            user_dict["user_username"] = request.form["username"]
            user_dict["user_pass"] = request.form["pass"]
            user_dict["user_id"] = new_user.id
            return redirect(url_for('apiget', action="event"))
        except Exception as e:
            return redirect(url_for('apiget', action="user"))

    if request.form["action"] == "event_update":
        try:    
            new_event = Event.add_event(user_dict["user_id"], request.form["name"], request.form["date"], request.form["time_s"], request.form["time_e"])
            return redirect(url_for('apiget', action="event"))  
        except Exception as e:
            return redirect(url_for('apiget', action="event"))
    
    
@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    ev_plot = Event.event_plot(user_dict["user_id"])
    xs = [el[0] for el in ev_plot]
    ys = [el[1] for el in ev_plot]
    axis.plot(xs, ys)
    return fig
       
    
if __name__ == '__main__':
    user_dict = {'user_name': 'Name',
                 'user_username': 'Username',
                 'user_pass': 102,
                 'user_id': 133}
    app.run()