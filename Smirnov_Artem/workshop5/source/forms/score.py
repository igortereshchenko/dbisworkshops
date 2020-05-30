from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import SelectField,StringField, IntegerField, SubmitField, RadioField, validators, ValidationError,FloatField
from wtforms.validators import InputRequired, NumberRange

class ScoreForm(FlaskForm):
	subjects_name =['Українська мова та література',
				'Математика',
				'Фізика',
				'Хімія',
				'Іноземна мова',
				'Історія України',
				'Географія',
				'Біологія',				
				'Бал за успішне закінчення підготовчих курсів закладу освіти']

	score_name = SelectField("Name: ",choices=[(name,name) for name in subjects_name])
	score_value = FloatField('Input your score',validators=[InputRequired(), NumberRange(min=110,max = 200, message='Enter a valid number')])
	# student_abitur = RadioField('Are you an abiturient?', coerce=int, choices=[(1, 'True'), (0, 'False')])

	submit_score = SubmitField("Add score")