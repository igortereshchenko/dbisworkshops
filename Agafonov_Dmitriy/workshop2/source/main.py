from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/api/<action>', methods=[ 'GET'])
def get_api(action):

   if action == "user":
      return render_template("user.html", user=user_dictionary)

   elif action == "question":
      return render_template("question.html", question=question_dictionary)

   elif action == "all":
      return render_template("all.html", user=user_dictionary, question=question_dictionary)

   else:
      return render_template("404.html", action_value=action)


@app.route('/api/user/submit', methods= ['POST'])
def user_submit():
    if(request.method == 'POST'):
        return str("User ID: ") + str(request.form['user_id'])+" <br>"+str("User Email: ")+str(request.form['user_email'])+" <br>"+str("User ЕДРПОУ code: ")+str(request.form['user_code'])+" <br>"+str("User PAssword: ") +str(request.form['user_password'])


@app.route('/api/question/submit', methods= ['POST'])
def question_submit():
    if(request.method == 'POST'):
        return str("Question ID: ")+str(request.form['question_id'])+"<br> "+str("Question time: ")+str(request.form['question_time'])+"<br> "+str("Question content: ")+str(request.form['question_content'])


if __name__ == '__main__':

   user_dictionary = {
            "user_id": "0001",
            "user_email": "qwerty@kpi.ua",
            "user_code": "123456789",
            "user_password": "123",
          }

   question_dictionary = {
            "question_id": "01",
            "question_time": "05022020",
            "question_content": "jcsdljckdsvjlaksv",
         }

   app.run(port=5001, debug=True)