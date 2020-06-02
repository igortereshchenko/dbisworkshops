from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Manga_Form(FlaskForm):
    manga_name = StringField('Manga Name')
    author = StringField('Author')
    year = StringField('Year')
    No_Toms = StringField('Number of chapters')
    submit = SubmitField('Submit')

class Anime_Form(FlaskForm):
    anime_name = StringField('Anime Name')
    date = StringField('Date')
    No_series = StringField('Number of episodes')
    genre = StringField('Genre')
    submit = SubmitField('Submit')



