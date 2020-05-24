from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField, IntegerField

class UserForm(FlaskForm):
    username = StringField('Username: ', validators=[validators.DataRequired('Required')])
    password = PasswordField('Password: ', validators=[validators.DataRequired('Required')])
    login = StringField('login: ', validators=[validators.DataRequired('Required')])
    name = StringField('name: ')
    surname = StringField('surname: ')
    faculty = StringField('faculty: ', validators=[validators.DataRequired('Required')])
    course = IntegerField('course: ', validators=[validators.DataRequired('Required')])

    back = SubmitField('<- Back')
    addbutton = SubmitField('Add')


