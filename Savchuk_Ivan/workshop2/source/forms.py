from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EntityForm(FlaskForm):
    pet_name = StringField('Pet name')
    color = StringField('Pet color')
    weight = StringField('Pet weight(kg)')
    height = StringField('Pet height(cm)')
    ability = StringField('Pet ability')
    submit = SubmitField('Submit')
