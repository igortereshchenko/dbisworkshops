from flask import Flask, render_template, request,  redirect, url_for
app = Flask(__name__)


@app.route('/', methods = ['GET'])
def start_page():
    return render_template("main.html", user=user)

@app.route('/api/<action>', methods = ['GET'])
def actinfo(action):
    if action == "user":

        return render_template("user.html", user=user)

    elif action == "note":
        return render_template("note.html", note=note)

    elif action == "all":
        return render_template("all.html", user=user, note=note)

    else:
        return render_template("404.html", action=action, user=user, note=note)



@app.route('/api', methods=['POST'])
def update():

   if request.form["action"] == "user_update":

      user["username"] = request.form["username"]
      user["id"] = request.form["id"]

      return redirect(url_for('actinfo', action="all"))

   if request.form["action"] == "note_update":

      note["id"] = request.form["id"]
      note["title"] = request.form["title"]
      note["text"] = request.form["text"]

      return redirect(url_for("actinfo", action="all"))




if __name__ == '__main__':
    note = {
        "id": "1",
        "title": "Some Title",
        "text": "Some text"
    }
    user = {
        "id": "1",
        "username": "UserName",
        "country": "Some Country"
    }

    app.run(use_reloader=False, debug=True)

