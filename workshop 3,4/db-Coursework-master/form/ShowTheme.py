from flask_wtf import FlaskForm
from wtforms import  SubmitField, RadioField,StringField, validators

class ThemeShow(FlaskForm):
    theme = StringField('Theme: ')
    theme_list = RadioField("List of Themes", coerce=int)
    back = SubmitField('<- Back')
    delete = SubmitField('Delete')
    choose = SubmitField('Choose')
    add = SubmitField('Add')
    update = SubmitField('update')
    filtering = SubmitField(' filter by Theme: ')
