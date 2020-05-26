from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from sqlalchemy.orm import sessionmaker

from dao.DB_connection import engine
from forms.wtf_form import  GetHealsParamForm
from dao.ORM_tables import Status, MediacalRecord


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ThisIam'

Session = sessionmaker(bind=engine)
session = Session()


@app.route('/form', methods=['GET', 'POST'])
def form():

	form = GetHealsParamForm()

	if form.validate_on_submit():
		
		new_record = Status(

			gender = form.gender.data,
			education = form.education.data,
			smoker = form.smoker.data,
			sigs_per_day = form.sigs_per_day.data,
			blood_pressure = form.blood_pressure.data,
			prevalent_stroke = form.prevalent_stroke.data,
			prevalent_hyp = form.prevalent_hyp.data,
			diabetes = form.diabetes.data,

			medical_record = [ MediacalRecord(

				tot_chol = form.tot_chol.data,
				sys_bp = form.tot_chol.data,
				dia_bp = form.dia_bp.data,
				body_index = form.body_index.data,
				heart_rate = form.heart_rate.data,
				glucose = form.glucose.data

			)]
		)

		session.add(new_record)
		session.commit()

		return '<h1>New data added</h1>'

	return render_template('medical_wtf.html', form=form)


if __name__ == '__main__':
	app.run(debug = True)