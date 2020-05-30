from flask_wtf import FlaskForm
from wtforms import StringField,   SubmitField,  PasswordField
from wtforms.validators import DataRequired

class SearchToken(FlaskForm):
    user_token = StringField("Token: ", validators = [
        DataRequired("Please enter your token.")
    ])

    user_password = PasswordField("Password: ", validators = [
        DataRequired("Please enter your password."),
    ])

    submit = SubmitField("Search")


    """
    def get_result(self):
        helper = TokenFinder()
        return helper.getTokenData(self.token_name.data)
    """