from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField
from wtforms.validators import InputRequired, NumberRange


class GetHealsParamForm(FlaskForm):

	gender = SelectField('Ваша стать', choices=[('male', 'чоловік'), ('female', 'жінка')])
	age = IntegerField('Ваш вік', validators=[InputRequired(), NumberRange(max = 130, message='Entere valid number')])
	education = SelectField('Здобута освіта', choices=[
		
		('SHS', 'Неповна загальноосвітня освіта'), ('HSoH', 'Повна загальноосвітня освіта'), 
		('SCoVS', 'Професійно-технічна освіта'), ('U', 'Вища освіта')
	
	])

	smoker = SelectField('Курець', choices=[('n', 'Ні'), ('y', 'Так')])
	sigs_per_day = IntegerField('Кількість сигарет кожного дня', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	blood_pressure = SelectField("Проблеми з кров'яним тиском", choices=[('n', 'Ні'), ('y', 'Так')])
	prevalent_stroke = SelectField('Інсульт', choices=[('n', 'Ні'), ('y', 'Так')])
	prevalent_hyp = SelectField('Гіпертонія', choices=[('n', 'Ні'), ('y', 'Так')])
	diabetes = SelectField('Діабет', choices=[('n', 'Ні'), ('y', 'Так')])

	tot_chol = DecimalField('Рівень холестерину (mg/dL)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	sys_bp = DecimalField("Систолічний кров'яний тиск (mmHh)", validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	dia_bp = DecimalField("Діастолічний кров'яний тиск (mmHh)", validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	body_index = DecimalField('Індекс маси тіла (кг/м2)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	heart_rate = IntegerField('Пульс (удар/хв)', validators=[InputRequired(), NumberRange(max = 99, message='Entere valid number')])
	glucose = DecimalField('Рівень глюкози (mg/dL)', validators=[InputRequired(), NumberRange(max = 999, message='Entere valid number')])
	