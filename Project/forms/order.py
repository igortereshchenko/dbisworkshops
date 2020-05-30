from flask_wtf import Form
from wtforms import SubmitField, validators, ValidationError, IntegerField


class CleanOrder(Form):
	submit = SubmitField("Удалить все")


class PushOrder(Form):
	submit = SubmitField("Оплатить заказ")


class Purchase(Form):
	submit = SubmitField("Оплата")


class Cancel(Form):
	submit = SubmitField("Отменить")