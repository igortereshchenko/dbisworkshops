from flask_wtf import FlaskForm
from wtforms import  SubmitField, RadioField

class UserShow(FlaskForm):
    user_list = RadioField("List of Users", coerce=int)
    back = SubmitField('<- Back')
    delete = SubmitField('Delete')

