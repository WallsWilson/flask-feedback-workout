from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class Register(FlaskForm):
    name = StringField('Username')
    pwd = PasswordField('Password')
    email = StringField('Email')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')

class Login(FlaskForm):
    name = StringField('Username')
    pwd = PasswordField('Password')