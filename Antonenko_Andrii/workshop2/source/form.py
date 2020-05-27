from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class UserForm(FlaskForm):
    user_id = StringField('User ID')
    user_first_name = StringField('User first name')
    user_last_name = StringField('User last name')
    user_email = StringField('User email')
    submit = SubmitField('Submit')


class DashboardForm(FlaskForm):
    dashboard_id = StringField('Dashboard ID')
    dashboard_name = StringField('Dashboard name')
    dashboard_user_id = StringField('Dashboard user id')
    submit = SubmitField('Submit')
