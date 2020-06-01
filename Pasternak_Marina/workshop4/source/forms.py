class UserForm(FlaskForm):
    name = StringField("First Name and Last Name: ")
    email = StringField("User email: ")
    password = StringField("User password: ")
    
    submit = SubmitField("Sign in")
