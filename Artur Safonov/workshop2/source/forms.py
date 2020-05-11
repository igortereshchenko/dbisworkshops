from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class UserForm(FlaskForm):
    name = StringField("Ім'я", [validators.DataRequired()])
    surname = StringField("Прізвище", [validators.DataRequired()])
    middle_name = StringField("По-батькові", [validators.DataRequired()])
    phone = StringField("Номер телефона", [validators.DataRequired()])
    email = StringField("Email")
    submit = SubmitField('OK')


class CardForm(FlaskForm):
    number = StringField("Номер карти", [validators.DataRequired()])
    name = StringField("Ім'я на картці", [validators.DataRequired()])
    date = StringField("Дата закінчення терміну дії картки", [validators.DataRequired()])
    cvv = PasswordField("CVV", [validators.DataRequired()])
    submit = SubmitField('OK')
