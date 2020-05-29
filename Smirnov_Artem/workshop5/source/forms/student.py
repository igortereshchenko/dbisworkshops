from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators, ValidationError
from wtforms.validators import InputRequired, NumberRange,Length

class StudentForm(FlaskForm):
	
	student_name = StringField("Name: ",validators=[InputRequired(), Length(min=3, max=100, message='Enter a valid name.Length from 3 to 100')])
	student_sex = SelectField('Your sex: ',choices=[('male','Male'),('female','Female')],validators=[InputRequired()])
	student_abitur = SelectField('Are you an abiturient?', coerce=int, choices=[(1, 'True'), (0, 'False')],validators=[InputRequired()])

	submit_student = SubmitField("Register")