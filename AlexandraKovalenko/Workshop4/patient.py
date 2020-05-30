from flask_wtf import FlaskForm
from wtforms import StringField,   SubmitField,  PasswordField, DateField, HiddenField
from wtforms import validators

class PatientForm(FlaskForm):
    id = HiddenField()

    username = StringField("Юзернейм: ", [validators.DataRequired("обов'язково"), validators.Length(3, 36),validators.regexp('@([a-z]*|[A-Z]*|_*|[0-9]*)*', message="@")])

    hirurg = StringField("Відділення хірургії: ", [validators.DataRequired("обов'язково"),validators.Length(10, 20)])

    lor = StringField("Відділення лор: ", [validators.DataRequired("обов'язково"),validators.Length(10, 20)])

    cardiolog = StringField("Відділення кардіології: ", [validators.DataRequired("обов'язково"),validators.Length(10, 20)])

    privivki = StringField("Відділення вакцинації", [validators.DataRequired("обов'язково"),validators.Length(10, 20)])

    submit = SubmitField("Зберегти")