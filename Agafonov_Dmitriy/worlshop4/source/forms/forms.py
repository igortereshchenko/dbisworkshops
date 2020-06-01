from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, DateTimeField


class SignUpForm(FlaskForm):
    
    user_name = StringField("user_name: ")
    user_mail = StringField("user_email: ")
    user_age = StringField("user_age: ")
    edrpou = StringField("edrpou: ")
    user_pass = PasswordField("user_password: ")
    submit = SubmitField("OK")


class CreateQuestion(FlaskForm):
    
    user_id = IntegerField("user_id: ")
    question_reference = StringField("question_reference: ")
    question = TextAreaField("question: ")
    time_creating = DateTimeField("time: ")
    submit = SubmitField("OK")