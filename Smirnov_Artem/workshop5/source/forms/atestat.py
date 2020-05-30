from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import SelectField,StringField, IntegerField, SubmitField, RadioField, validators, ValidationError,FloatField
from wtforms.validators import InputRequired, NumberRange

class AtestatForm(FlaskForm):
	atestat_value = FloatField('Середній бал документа про освіту',validators=[InputRequired(), NumberRange(min=1,max = 12, message='Enter a valid number')])
	
	submit_atestat = SubmitField("Add score")