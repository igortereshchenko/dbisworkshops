from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField, TextAreaField


class ContactForm(FlaskForm):
    message = StringField("message: ")
    customer_name = StringField("customer_name: ")
    age = IntegerField("age: ")
    email = StringField("email: ")
    tour_name = StringField("tour_name: ")
    submit = SubmitField("Submit")


class Feedback(FlaskForm):
    tour_name = StringField("tour_name: ")
    group_name = StringField("group_name: ")
    feedback_message = TextAreaField("feedback_message: ")
    submit = SubmitField("Submit")

class FindTour(FlaskForm):
    country = StringField('country:')
    year_category = SelectField('category', choices=[('summer tour', 'summer tour'), ('autumn tour', 'autumn tour'), ('winter tour', 'winter tour'), ('spring tour', 'spring tour')])
    tour_duration = SelectField('duration', choices=[('3 days', '3 days'), ('5 days', '5 days'), ('7 days', '7 days'), ('10 days', '10 days')])
    price_range = SelectField('price_range', choices=[('100-500 dollars', '100-500 dollars'), ('500-1000 dollars', '500-1000 dollars'), ('1000+ dollars', '1000+ dollars')])
    submit = SubmitField("Submit")






