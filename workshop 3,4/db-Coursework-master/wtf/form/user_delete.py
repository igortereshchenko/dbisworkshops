from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class UserDelete(FlaskForm):
    deleteUser = StringField('deleteUser: ', validators=[validators.DataRequired('Required')])
    deletebutton = SubmitField('Delete')