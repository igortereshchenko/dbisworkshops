from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, TextAreaField, IntegerField, DateTimeField, FloatField


class ExpenditureForm(FlaskForm):
    time = StringField("current_data:")
    cost_value = FloatField("cost_value:")
    category_name = StringField("category_name: ")
    card_number = IntegerField("card_number:")
    submit = SubmitField("OK")

class CreateCard(FlaskForm):
    card_number = IntegerField("card_number:")
    money_amount = IntegerField("money_amount:")
    submit = SubmitField("OK")

class Monitor(FlaskForm):
    time = StringField('current_data:')
    category_name= SelectField('category', choices=[('food', 'food'), ('clothes', 'clothes'),
                                                     ('medecine', 'medecine'), ('travel', 'travel'), ('enrertaiment', 'enrertaiment')])
    submit = SubmitField("OK")