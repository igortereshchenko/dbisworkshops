from flask import Flask, render_template, request,flash
from flask_sqlalchemy import SQLAlchemy
from forms.student import StudentForm
# from dao import db_api
from orm.database_connection import ENGINE_PATH_WIN_AUTH
from orm.create_table import Students


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ENGINE_PATH_WIN_AUTH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sausage'

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def user():
    form = StudentForm(request.form)


    # allUsers = getUsers()

    if request.method == 'POST':
        print(request.form['student_name'],request.form['student_sex'])
        print(form.validate())  
        print(form.errors)  
        if form.validate():
            #add by cx_oracle
            # db_api.newUser(request.form['student_name'],
            #                 request.form['student_abitur'],
            #                 request.form['student_sex'])
            # #add by orm
            db.session.add(Students(student_name=request.form['student_name'],
                                    student_sex=request.form['student_sex'],
                                    student_abitur=bool(int(request.form['student_abitur']))))
            db.session.commit()
            return render_template('index.html', form=form)
        else:

            return render_template('index.html', form=form)


    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)