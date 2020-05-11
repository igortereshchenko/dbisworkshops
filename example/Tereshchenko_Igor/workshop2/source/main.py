from flask import Flask, render_template, request, abort,  redirect, url_for
app = Flask(__name__)


@app.route('/api/<action>', methods = ['GET'])
def apiget(action):
    if action == "student":

        return render_template("student.html", student=student)

    elif action == "book":
        return render_template("book.html", book=book)

    elif action == "all":
        return render_template("all.html", student=student, book=book)

    else:
        return render_template("404.html", action=action, student=student, book=book)



@app.route('/api', methods=['POST'])
def update():

   if request.form["action"] == "student_update":

      student["username"] = request.form["username"]
      student["id"] = request.form["id"]

      return redirect(url_for('apiget', action="all"))

   if request.form["action"] == "book_update":

      book["title"] = request.form["title"]
      book["dish_name"] = request.form["author"]
      book["year"] = request.form["year"]

      return redirect(url_for("apiget", action="all"))




if __name__ == '__main__':
    book = {
        "title": "title_1",
        "author": "author_1",
        "year": 1994

    }
    student = {
        "username": "Bob",
        "id": "1"

    }

    app.run(debug=True)


