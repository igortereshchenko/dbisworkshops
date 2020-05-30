from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, DecimalField, SubmitField, TextAreaField,\
					validators, ValidationError


class CafeAddForm(Form):
	cafe_name = StringField("Название кафе: ")
	cafe_popularity = DecimalField("Популярность:")

	submit = SubmitField("Добавить")

