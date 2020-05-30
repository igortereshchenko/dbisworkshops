from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, DateTimeField


class ExpenditureForm(FlaskForm):
    cost_value = IntegerField("cost_value:")
    time = time_creating = DateTimeField("time: ")
    category_name = StringField("category_name: ")
    card_number = IntegerField("card_number:")
    submit = SubmitField("OK")

class CreateCard(FlaskForm):
    card_number = IntegerField("card_number:")
    money_amount = IntegerField("money_amount:")
    submit = SubmitField("OK")
