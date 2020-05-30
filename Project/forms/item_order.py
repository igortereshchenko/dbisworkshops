from flask_wtf import Form
from wtforms import SubmitField, validators, ValidationError, IntegerField


class AddToOrder(Form):
	cafe_id = IntegerField()
	item_id = IntegerField()
	item_amount = IntegerField()
	submit = SubmitField("Добавить")
