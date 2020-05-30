from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import StringField, DecimalField, SubmitField, TextAreaField,\
					validators, ValidationError, SelectField



class DishAddForm(Form):

	cafe_id = SelectField("Название кафе: ", choices=[("1", "McDonald’s"), ("2", "KFC"), ("3", "Shawarma")])
	dish_name = StringField("Название блюда: ")
	dish_price = DecimalField("Цена блюда:")
	dish_describe = TextAreaField("Описание блюда:")
	dish_avg_time = DecimalField("Среднее время готовки:")

	submit = SubmitField("Добавить")