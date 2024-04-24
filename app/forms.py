from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
import email_validator
class RegisterForm(FlaskForm):
    email = EmailField("Введите ваш email:", [DataRequired("Поле не должно быть пустым"), Email("Введите правильный EMail")])
    password = PasswordField("Введите пароль:", [DataRequired("Поле не должно быть пустым")])
    repeat_password = PasswordField("Повторите ваш пароль", [DataRequired("Поле не должно быть пустым"), EqualTo("password", "Пароли не совпадают")])
    token = StringField("Введите токен человека, пригласившего вас")
    
    submit = SubmitField("Регистрация")


class LoginForm(FlaskForm):
    email = EmailField("Введите ваш email:", [DataRequired(), Email()])
    password = PasswordField("Введите пароль:", [DataRequired()])
    
    submit = SubmitField("Регистрация")