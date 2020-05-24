from flask_wtf import FlaskForm
from wtforms import SubmitField

class first_page(FlaskForm):
    auth = SubmitField("Authorization")
    reg = SubmitField("Registration")
    logout = SubmitField("Log out")
    show_theme = SubmitField("Choose theme")
    show_resourse = SubmitField("Choose resourse")
    show_info = SubmitField("Get info")
    show_user = SubmitField("Show all users")
    show_stat = SubmitField("Show statistic")