from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, IntegerField, SubmitField, FloatField, DateTimeField

class SingInForm(FlaskForm):
    nickname = StringField("nickname: ")
    age = IntegerField("age: ")
    phone = StringField("phone: ")
    password = PasswordField("password: ")
    submit = SubmitField("Submit")

class ValidationForm(FlaskForm):
    code = StringField("code: ")
    submit = SubmitField("Submit")

class EventSelection(FlaskForm):
    event_name = SelectField('event', choices=[])
    submit = SubmitField("Submit")

class PurchaseForm(FlaskForm):
    price = StringField("price: ")
    tickets_left = IntegerField("tickets left: ")
    event_time = DateTimeField("event time: ")
    submit = SubmitField("Submit")

class SuccessForm(FlaskForm):
    submit = SubmitField("Go next")