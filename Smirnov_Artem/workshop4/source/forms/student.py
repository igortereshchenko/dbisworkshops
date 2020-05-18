from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, SubmitField, RadioField, validators, ValidationError

class StudentForm(Form):
	
	student_name = StringField("Name: ")
	student_sex = RadioField('Your sex: ',choices=[('male','Male'),('female','Female')])
	student_abitur = RadioField('Are you an abiturient?', coerce=int, choices=[(1, 'True'), (0, 'False')])

	submit = SubmitField("Register")