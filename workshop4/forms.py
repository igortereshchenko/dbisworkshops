from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, FloatField


class HikeForm(FlaskForm):
    hike_name = StringField('User name')
    duration = IntegerField('Duration')
    complexity = IntegerField('Complexity')
    length = FloatField('Length')
    price = IntegerField('Price')

    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    fio = StringField('FIO')
    birth_date = DateField('Birth date in format yyyy.mm.dd')
    equipment = IntegerField('Equipment')
    healthy = IntegerField('Healthy')
    height = FloatField('Height')
    weight = FloatField('eight')

    submit = SubmitField('Submit')


class OrderForm(FlaskForm):
    fk_user_id = IntegerField('User ID')
    fk_sentence_id = IntegerField('Sentence ID')

    submit = SubmitField('Submit')


class SentenceForm(FlaskForm):
    fk_hike_id = IntegerField('Hike ID')
    start_date = DateField('Start date in format yyyy.mm.dd')

    submit = SubmitField('Submit')
