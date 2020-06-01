import datetime
import sqlalchemy

from flask import Flask
from flask import request
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.ORM_tables import Doctor, Hospital, Timetable
from forms.WTForms import Registration

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Alex'

oracle_connection_string = 'oracle+cx_oracle://system:oracle@localhost:1521/xe'
engine = create_engine(oracle_connection_string, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/registration', methods=["GET", "POST"])
def regist():
    form = Registration()
    if form.is_submitted():
#        try:
        result = request.form
        print(result['time_date'])
        adddata = Timetable(doc_id=result['doc_id'], hosp_name=result['hosp_name'], pat_name=result['pat_name'],
                            pat_age=result['pat_age'], pat_street=result['pat_street'], pat_dist=result['pat_dist'],
                            time_date=result['time_date'])
        session.add(adddata)
        session.commit()
        return render_template('good_confirm.html', result=result)

#        except:
#            result = request.form
#            return render_template('bad_confirm.html', result=result)

    return render_template('registration.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)