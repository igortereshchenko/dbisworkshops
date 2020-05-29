from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, IntegerField, SubmitField, DateTimeField, FieldList, FormField

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

class LoginForm(FlaskForm):
    nickname = StringField("nickname")
    password = PasswordField("password")
    submit = SubmitField("Submit")
    signin = SubmitField("Sign UP")

class EventForm(FlaskForm):
    name = StringField()
    tickets_left = StringField()
    time = StringField()
    price = StringField()

class AdminForm(FlaskForm):
    events = FieldList(FormField(EventForm))
    submit = SubmitField("Add event")
    stats = SubmitField("Stats")

class AddEventForm(FlaskForm):
    event_id = IntegerField()
    event_name = StringField()
    event_tag = StringField()
    reg_date_start = DateTimeField()
    reg_date_finish = DateTimeField()
    tickets_left = IntegerField()
    event_time = DateTimeField()
    price = IntegerField()
    submit = SubmitField()
