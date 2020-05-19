from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField


class UserForm(FlaskForm):
    first_name = StringField('User first name', [validators.required(), validators.length(max=32, min=2)])
    last_name = StringField('User last name', [validators.required(), validators.length(max=32, min=2)])
    email = StringField('User email', [validators.required(), validators.email()])
    submit = SubmitField('Submit')


class GroupForm(FlaskForm):
    name = StringField('Group name', [validators.required(), validators.length(min=2, max=32)])
    submit = SubmitField('Submit')


class AddUserToGroup(FlaskForm):
    user_email = StringField('User email', [validators.email()])
    group_name = StringField('Group name', [validators.required(), validators.length(min=2, max=32)])
    role = SelectField('Role', choices=[('owner', 'Owner'), ('participant', 'Participant'), ('guest', 'Guest')])
    submit = SubmitField('Submit')
