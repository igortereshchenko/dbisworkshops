from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SongForm(FlaskForm):
    song_name = StringField('Song name')
    artist = StringField('Artist')
    date_of_release = StringField('Date of release')
    submit = SubmitField('Submit')

class OrderForm(FlaskForm):
    id = StringField('ID')
    order_text = StringField('Order text')
    submit = SubmitField('Submit')