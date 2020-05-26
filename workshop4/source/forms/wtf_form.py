from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField
from wtforms.validators import InputRequired, NumberRange


class GetHealsParamForm(FlaskForm):

	gender = SelectField('gender', choices=[('male', 'male'), ('female', 'female')])
	education = SelectField('education', choices=[
		
		('SHS', 'Some High School'), ('HSoH', 'Hight School or GED'), 
		('SCoVS', 'Some College or Vocational School'), ('C', 'College')
	
	])

	smoker = SelectField('smoker', choices=[('y', 'Yes'), ('n', 'No')])
	sigs_per_day = IntegerField('bigs per day')
	blood_pressure = SelectField('blood pressure', choices=[('y', 'Yes'), ('n', 'No')])
	prevalent_stroke = SelectField('prevalent stroke', choices=[('y', 'Yes'), ('n', 'No')])
	prevalent_hyp = SelectField('prevalent hypertony', choices=[('y', 'Yes'), ('n', 'No')])
	diabetes = SelectField('diabetes', choices=[('y', 'Yes'), ('n', 'No')])

	tot_chol = DecimalField('total cholesterol level (mg/dL)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	sys_bp = DecimalField('systolic blood pressure (mmHh)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	dia_bp = DecimalField('diastolic blood pressure (mmHh)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	body_index = DecimalField('body Mass Index (kg/m2)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	heart_rate = IntegerField('heart rate (beats/min)', validators=[InputRequired(), NumberRange(max = 99, message='Entere valid number')])
	glucose = DecimalField('glucose level (mg/dL)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	