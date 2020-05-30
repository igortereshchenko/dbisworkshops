from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, IntegerField, SubmitField, TextAreaField,\
					validators, ValidationError, SelectField
from orm.database_connection import engine
# from dao import db_api


class OrderAddForm(Form):

	#choices = [('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
	#choices = db_api.get_all_dishes()
	con = engine.connect()
	query_res = con.execute(" SELECT dish_id, dish_name FROM DISHES; ")
	print("Choices", query_res)

	choices = []
	for row in query_res:
		choices.append((row["dish_id"], row["dish_name"]))
	print("Choices", choices)
	dish_id = SelectField('Name of dish',coerce=int, choices=choices)
	user_name = StringField("Your name: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 				])
	user_phone = StringField('Input yout phone')
	amount_dishes = IntegerField('Input how many ')

	submit = SubmitField("Add a dish")

