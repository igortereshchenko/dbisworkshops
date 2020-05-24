from flask_wtf import FlaskForm
from wtforms import  SubmitField, RadioField,StringField

class InfoShow(FlaskForm):
    info = StringField('Info: ')
    info_list = RadioField("List of Resourse: ", coerce=int)
    back = SubmitField('<- Back')
    delete = SubmitField('Delete')
    add = SubmitField('Add')
    filter_n = StringField('by nickname: ')
    filter_T = StringField('by theme: ')
    filtering = SubmitField('filtered by: ')