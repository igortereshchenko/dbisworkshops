from flask import Flask, render_template, request, redirect, url_for
import random
import hashlib

def hashing():
    string = str(user_dictionary["user_id"]) + user_dictionary["user_name"] + user_dictionary["user_surname"] + user_dictionary["user_email"] + str(user_dictionary["user_phone_number"])
    mix = ''.join(random.sample(string,len(string)))
    result = hashlib.sha256(mix.encode())
    return result.hexdigest()

app = Flask(__name__)


@app.route("/", methods = ['GET'])
def hello():
  return (
    {
      "rt": "/",
      "sub_rt":{
            "alldata":"/api/all",
            "users": "/api/user",
            "tokens":"/api/token",
          }
    }
  )

@app.route('/api/<action>', methods = [ 'GET'])
def apiget(action):

   if action == "user":
      return render_template("user.html",user=user_dictionary)

   elif action == "token":
      return render_template("token.html", token=token_dictionary)

   elif action == "all":
      return render_template("all.html", user=user_dictionary, token = token_dictionary)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api', methods=['POST'])
def apipost():
   if request.form["action"] == "user_update":
       if user_dictionary["user_name"] == request.form["name"] and user_dictionary["user_surname"] == request.form["surname"] and user_dictionary["user_email"] == request.form["email"] and user_dictionary["user_phone_number"] == request.form["phone"]:
           return redirect(url_for('apiget', action="token"))
       else:
           user_dictionary["user_name"] = request.form["name"]
           user_dictionary["user_surname"] = request.form["surname"]
           user_dictionary["user_email"] = request.form["email"]
           user_dictionary["user_phone_number"] = request.form["phone"]
           token_dictionary["user_token"] = hashing()
           return redirect(url_for('apiget', action="token"))

   if request.form["action"] == "token_update":
        token_dictionary["user_token"] = hashing()
        return redirect(url_for('apiget', action="token"))

if __name__ == '__main__':

   user_dictionary = {
            "user_id": 1001,
            "user_name": "Paul",
            "user_surname": "Smith",
            "user_email":"paul_smith1979@mail.com",
            "user_phone_number": 4379201365,
            "user_end_date": "12-08-2020",
          }

   token_dictionary = {
           "user_id": 1001,
           "user_token": "c2e037aa1862a7b44bafca44ff0bb5848c75d2b07147bbcc261814ccaf5eb161",
           "user_qr_code": "1001id_qrcode.png",
         }

   app.run(port = 5001, debug = True)