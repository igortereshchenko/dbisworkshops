from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_dict = {
    "id": "1",
    "username": "UserName",
    "lang_code": "en"
}

message_dict = {
    "id": "1",
    "sender_id": "1",
    "receiver_id": "2",
    "text": ''
}


@app.route('/', methods=['GET'])
def main_page():
    return render_template("main.html")


@app.route('/api/<action>', methods=['GET'])
def api_get(action):
    if action == "user":
        return render_template("user.html", user=user_dict)

    elif action == "message":
        return render_template("message.html", message=message_dict)

    elif action == "all":
        return render_template("all.html", user=user_dict, message=message_dict)

    else:
        return render_template("404.html", action=action)


@app.route('/api', methods=['POST'])
def api_post():
    if request.form["action"] == "user_update":
        user_dict["id"] = request.form["id"]
        user_dict["username"] = request.form["username"]
        user_dict["lang_code"] = request.form["lang_code"]

        return redirect(url_for('api_get', action="all"))

    if request.form["action"] == "message_update":
        message_dict["id"] = request.form["id"]
        message_dict["sender_id"] = request.form["sender_id"]
        message_dict["receiver_id"] = request.form["receiver_id"]
        message_dict["text"] = request.form["text"]

        return redirect(url_for('api_get', action="all"))


if __name__ == '__main__':

    app.run(debug=True)
