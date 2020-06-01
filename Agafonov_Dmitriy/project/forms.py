from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, SelectField, DateTimeField
from wtforms import validators
from wtforms.validators import InputRequired, Regexp, ValidationError




class SignUpForm(FlaskForm):
    user_name = StringField("username ", [validators.InputRequired(), validators.Length(min=4, max=25), validators.Regexp('^\w+$',
                                                                                          message="Username must contain only letters numbers or underscore")])
    user_mail = StringField("email ", [validators.DataRequired(), validators.Email()])
    user_age = IntegerField("age ", validators=[InputRequired()])
    edrpou = StringField("edrpou code ", [validators.Length(min=16, max=16), validators.InputRequired()])
    user_pass = PasswordField("password ", [validators.InputRequired(), validators.Length(min=5, max=25)])
    submit = SubmitField("Sign up")

    def validate_username(self, user_mail):
        user = user_database.query.filter_by(username=user_mail.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, edrpou):
        user = user_database.query.filter_by(email=edrpou.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LogInForm(FlaskForm):
    user_mail = StringField("email ", [validators.DataRequired(), validators.Email()])
    user_pass = PasswordField("password ", validators=[InputRequired()])
    submit = SubmitField("Login")


class CreateQuestion(FlaskForm):
    user_id = IntegerField("user_id: ")
    question_reference = SelectField("question_reference: ",
                                     choices=[('1', 'lawyer'), ('2', 'economist'), ('3', 'accountant')])
    question = TextAreaField("question: ")
    time_creating = StringField("time: ")
    submit = SubmitField("OK")