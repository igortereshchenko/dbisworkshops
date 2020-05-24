from flask_wtf import FlaskForm
from wtforms import  SubmitField, RadioField,StringField, validators

class ResourseShow(FlaskForm):
    resourse = StringField('Resourse: ')
    resourse_list = RadioField("List of Resourse: ", coerce=int)
    back = SubmitField('<- Back')
    delete = SubmitField('Delete')
    choose = SubmitField('Choose')
    add = SubmitField('Add')
    update = SubmitField('update')
    filtering = SubmitField(' filter by Resourse: ')