from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField, DecimalField, TextAreaField


class DishForm(FlaskForm):
    name = StringField("Название: ")
    price = DecimalField("Цена (за порцию): ")
    taste = SelectField("Вкус: ", choices=[("1", "Сладкое"), ("2", "Соленое"), ("3", "Кислое"), ("4", "Другое")])
    risk_name = SelectField("Противопоказания: ", choices=[("1", "Цитрусовые"), ("2", "Молочные продукты"),
                                                           ("3", "Рыба"), ("4", "Другое")])

    submit = SubmitField("Готово")

