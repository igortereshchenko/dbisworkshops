from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class HikeForm(FlaskForm):
    hike_name = StringField('Hike name')
    during = StringField('During')
    km = StringField('Km')
    complexity = StringField('complexity')
    start_date = StringField('Start date')
    cost = StringField('Cost')
    submit = SubmitField('Submit')

class UserForm(FlaskForm):
    user_name = StringField('User name')
    weight = StringField('weight')
    height = StringField('height')
    birth_date = StringField('Birth date')
    diseases = StringField('diseases')
    submit = SubmitField('Submit')