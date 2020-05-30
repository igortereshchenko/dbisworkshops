from flask_wtf import FlaskForm
from wtforms import StringField,   SubmitField,  PasswordField, HiddenField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from dao.orm.model import ormUser

import phonenumbers

class RegistrationForm(FlaskForm):
    user_id = HiddenField()

    user_name = StringField("Name: ", validators = [
        DataRequired("Please enter your name."),
        Length(3, 20, "Name should be from 3 to 15 symbols")
    ])

    user_surname = StringField("Surname: ", validators = [
        DataRequired("Please enter your surname."),
        Length(3, 20, "Surname should be from 3 to 20 symbols")
    ])

    user_email = StringField("Email: ", validators = [
        DataRequired("Please enter your email."),
        Email("Wrong email format"),
    ])

    user_phone = StringField("Phone number: ", validators = [
    ])

    user_password = PasswordField("Password: ", validators = [
        DataRequired("Please enter your password.")
    ])

    confirm_user_password = PasswordField("Confirm password: ", validators = [
        DataRequired(),
        EqualTo('user_password')
    ])

    agreement = BooleanField("I agree with our Privacy Policy", validators = [
        DataRequired("Please agree to continue.")
    ])

    end_date = HiddenField()

    submit = SubmitField("Submit!")

    # Can't understand how to make theese validators work with declarative_base().
    # Return AttributeError: type object 'ormUser' has no attribute 'filter_by'
    # I will try to fix it until Tuesday or Sunday evening

    def validate_user_email(self, user_email):
        pass
        user = ormUser.filter_by(user_email = user_email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose another one.')

    def validate_user_phone(self, user_phone):
        try:
            p = phonenumbers.parse(user_phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
            user = ormUser.query.filter_by(user_phone=user_phone.data).first()
            if user:
                raise ValidationError('That phone number is taken. Please choose another one.')
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')




