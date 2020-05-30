from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, DecimalField, SubmitField, TextAreaField,\
					validators, ValidationError


class DishAddForm(Form):
	
	dish_name = StringField("Name of a dish: ",[
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 				])
	dish_price = DecimalField("Write a price of a dish:")
	dish_describe = TextAreaField("Write a describe of a dish:")
	
	submit = SubmitField("Add a dish")