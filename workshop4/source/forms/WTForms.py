from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, DateTimeField


class Registration(FlaskForm):
    doc_id = IntegerField("doc_id of your doctor: ")
    hosp_name = StringField("hosp_name: ")
    pat_name = StringField("your name: ")
    pat_age = IntegerField("your age: ")
    pat_street = StringField("your street: ")
    pat_dist = StringField("your district: ")
    time_date = StringField("time: ")
    submit = SubmitField("OK")