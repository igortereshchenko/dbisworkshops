from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import SelectField,StringField, IntegerField, SubmitField, RadioField, validators, ValidationError
from orm.database_connection import engine

conn = engine.connect()

class SearchForm(FlaskForm):
	choices = [(row['region_id'],row['region_name']) for row in conn.execute('select region_id, region_name from regions;')]
	# print(choices)
	search_region = SelectField("Region: ",coerce=int,choices=choices)
	choices = conn.execute('select specialty_id, specialty_name from specialties')
	choices = [(row['specialty_id'], row['specialty_name']) for row in choices]
	search_specialty = SelectField("Specialty: ",coerce=int,choices=choices)
	# student_abitur = RadioField('Are you an abiturient?', coerce=int, choices=[(1, 'True'), (0, 'False')])

	submit_search = SubmitField("Search")