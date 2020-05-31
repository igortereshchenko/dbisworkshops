import cx_Oracle
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.ORM_tables import Timetable
from forms.WTForms import Registration, List
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Alex'

oracle_connection_string = 'oracle+cx_oracle://system:oracle@localhost:1521/xe'
engine = create_engine(oracle_connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()


def func(x):
    img = BytesIO()
    plt.bar('Сьогодні', x)
    plt.title('Кількість пацієнтів, які користувались нашим сервісом')
    plt.savefig(img, format="png")
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return "data:image/png;base64,{}".format(plot_url)


@app.route('/')
@app.route('/home', methods=["GET", "POST"])
def home():
    connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
    cursor = connection.cursor()
    query = "SELECT COUNT(unique(pat_name)) FROM timetable"
    cursor.execute(query)
    x = cursor.fetchone()[0]
    img = func(x)

    return render_template('home_page.html', img=img)


@app.route('/registration', methods=["GET", "POST"])
def regist():
    form = Registration()
    print(form)
    if form.is_submitted():
        try:
            result = request.form
            connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
            cursor = connection.cursor()
            query = "SELECT hosp_dist FROM hospital WHERE hosp_name = '{}'".format(result['hosp_name'])
            cursor.execute(query)
            data = cursor.fetchone()[0]

            if data==result['pat_dist']:
                cursor.close()
                connection.close()

                adddata = Timetable(doc_id=result['doc_id'], hosp_name=result['hosp_name'], pat_name=result['pat_name'],
                                    pat_age=result['pat_age'], pat_street=result['pat_street'], pat_dist=result['pat_dist'],
                                    time_date=result['time_date'])
                session.add(adddata)
                session.commit()
                return render_template('good_confirm.html', result=result)

            else:
                result = request.form
                return render_template('bad_confirm.html', result=result)

        except:
            result = request.form
            return render_template('bad_confirm.html', result=result)

    return render_template('registrations.html', form=form)


@app.route('/list', methods=["GET", "POST"])
def view():
    form = List()
    if form.is_submitted():
        try:
            result = request.form
            connection = cx_Oracle.connect('system/oracle@localhost:1521/xe')
            cursor = connection.cursor()
            query = """
                    SELECT
                        doctor.doc_name,
                        doctor.doc_special,
                        doctor.cabinet,
                        doctor.hosp_name,
                        hospital.hosp_address,
                        timetable.time_date
                    FROM
                        doctor
                        JOIN hospital ON doctor.hosp_name = hospital.hosp_name
                        JOIN timetable ON doctor.doc_id = timetable.doc_id
                                          AND hospital.hosp_name = timetable.hosp_name
                    WHERE
                        pat_name = '{}'
                        AND pat_street = '{}'
                    """.format(result['pat_name'], result['pat_street'])

            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
            connection.close()

            if not data:
                return render_template('no_data.html')
            else:
                return render_template('pat_data.html', data=data)

        except:
            return render_template('no_data.html')

    return render_template('lists.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)