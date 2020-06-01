from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField, DateTimeField
from wtforms import validators
from wtforms.validators import InputRequired, Regexp



class SignUpForm(FlaskForm):
    
    user_name = StringField("user_name: ", [validators.InputRequired(), validators.Regexp('^\w+$', message="Username must contain only letters numbers or underscore")])
    user_mail = StringField("user_email: ",  [validators.DataRequired(), validators.Email()])
    user_age = StringField("user_age: ", validators=[InputRequired()])
    edrpou = StringField("edrpou: ", [validators.Length(min=16, max=16), validators.InputRequired()])
    user_pass = PasswordField("user_password: ", validators=[InputRequired()])
    submit = SubmitField("OK")


class CreateQuestion(FlaskForm):
    
    user_id = IntegerField("user_id: ")
    question_reference = SelectField("question_reference: ", choices=[('1', 'lawyer'), ('2', 'economist'), ('3', 'accountant')])
    question = TextAreaField("question: ")
    time_creating = StringField("time: ")
    submit = SubmitField("OK")