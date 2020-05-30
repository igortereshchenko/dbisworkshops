from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)


@app.route('/api/<action>', methods=['GET'])
def apiget(action):
    if action == "all":
        users_list = list(users.keys())
        memberships_list = list(memberships.keys())
        return render_template("all.html", user=users, membership=memberships, u_list=users_list,
                               m_list=memberships_list)

    else:
        return render_template("404.html", action_value=action)


@app.route('/api/all', methods=['POST'])
def apipost_for_all():
    if request.form["check_update_user"] == "user_update_user":
        users_list = list(users.keys())
        for i in range(len(users_list)):
            users_list[i] = int(users_list[i])
        id = max(users_list) + 1
        id = str(id)
        users[id] = {}
        users[id]["user_link"] = '/api/user/{}'.format(id)
        users[id]["user_name"] = str(request.form["user_name"])
        users[id]["user_fullname"] = str(request.form["user_fullname"])
        users[id]["user_age"] = str(request.form["user_age"])
        users[id]["user_sex"] = str(request.form["user_sex"])
        users[id]["status"] = str(request.form["status"])
        users[id]["user_photo"] = str(request.form["user_photo"])

    elif request.form["check_update_user"] == "membership_update_membership":
        memberships_list = list(memberships.keys())
        for i in range(len(memberships_list)):
            memberships_list[i] = int(memberships_list[i])
        id = max(memberships_list) + 1
        id = str(id)
        memberships[id] = {}
        memberships[id]["membership_link"] = '/api/membership/{}'.format(id)
        memberships[id]["user_name"] = str(request.form["m_user_name"])
        memberships[id]["time"] = str(request.form["time"])
        memberships[id]["qr_code"] = str(request.form["qr_code"])
    users_list = list(users.keys())
    memberships_list = list(memberships.keys())
    with open("./database/users.json", "w", encoding='utf-8') as users_db, open("./database/memberships.json", "w",
                                                                                encoding='utf-8') as memberships_db:
        json.dump(users, users_db)
        json.dump(memberships, memberships_db)
    return render_template("all.html", user=users, membership=memberships, u_list=users_list,
                           m_list=memberships_list)


@app.route('/api/<action>/<id>', methods=['GET'])
def local_apiget(action, id):

    if action == "user":
        return render_template("user.html", user=users[id])
    elif action == "membership":
        return render_template("membership.html", membership=memberships[id])
    else:
        return render_template("404.html", action_value=action)


@app.route('/api/user/<id>', methods=['POST'])
def apipost_for_user(id):
    if request.form["check_update"] == "user_update":
        users[id]["user_name"] = request.form["user_name"]
        users[id]["user_fullname"] = request.form["user_fullname"]
        users[id]["user_age"] = request.form["user_age"]
        users[id]["user_sex"] = request.form["user_sex"]
        users[id]["status"] = request.form["status"]
        users[id]["user_photo"] = request.form["user_photo"]
        with open("./database/users.json", "w", encoding='utf-8') as users_db, open("./database/memberships.json", "w",encoding='utf-8') as memberships_db:
            json.dump(users, users_db)
            json.dump(memberships, memberships_db)
        return redirect(url_for('local_apiget', action="user", id=id))
    elif request.form["check_update"] == "user_delete":
        users.pop(str(id), None)
        users_list = list(users.keys())
        memberships_list = list(memberships.keys())
        with open("./database/users.json", "w", encoding='utf-8') as users_db, open("./database/memberships.json", "w",encoding='utf-8') as memberships_db:
            json.dump(users, users_db)
            json.dump(memberships, memberships_db)
        return redirect(url_for('apiget', action="all", user=users, membership=memberships, u_list=users_list,
                                m_list=memberships_list))


@app.route('/api/membership/<id>', methods=['POST'])
def apipost_for_membership(id):
    if request.form["check_update"] == "membership_update":
        memberships[id]["time"] = request.form["time"]
        with open("./database/users.json", "w", encoding='utf-8') as users_db, open("./database/memberships.json", "w",encoding='utf-8') as memberships_db:
            json.dump(users, users_db)
            json.dump(memberships, memberships_db)
        return redirect(url_for('local_apiget', action="membership", id=id))
    elif request.form["check_update"] == "membership_delete":
        memberships.pop(str(id), None)
        users_list = list(users.keys())
        memberships_list = list(memberships.keys())
        with open("./database/users.json", "w", encoding='utf-8') as users_db, open("./database/memberships.json", "w",encoding='utf-8') as memberships_db:
            json.dump(users, users_db)
            json.dump(memberships, memberships_db)
        return redirect(url_for('apiget', action="all", user=users, memberships=memberships, u_list=users_list,
                                m_list=memberships_list))


if __name__ == '__main__':
    with open("./database/users.json", "r", encoding='utf-8') as users_db, open("./database/memberships.json", "r",
                                                                                encoding='utf-8') as memberships_db:
        users = json.load(users_db)
        memberships = json.load(memberships_db)

    app.run()
