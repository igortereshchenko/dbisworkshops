from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField


class SetReviewForm(FlaskForm):
    text = StringField('Text')
    rate = IntegerField('Rate')
    submit = SubmitField('Submit')
