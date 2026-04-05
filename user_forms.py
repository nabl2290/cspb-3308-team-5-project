from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    first_name = StringField('First name', [
        validators.DataRequired(),
        validators.Length(max=50, message="First name cannot exceed 50 characters.")
    ])
    last_name = StringField('Last name', [
        validators.DataRequired(),
        validators.Length(max=50, message="Last name cannot exceed 50 characters.")
    ])
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Email(message="Please enter a valid email address."),
        validators.Length(max=120, message="Email cannot exceed 120 characters.")
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.Length(min=7, message="Password must be at least 7 characters long.")
    ])
    password_confirmed = PasswordField('Password Confirmation', [
        validators.DataRequired(),
        validators.EqualTo('password', message="Passwords do not match.")
    ])

class LoginForm(FlaskForm):
    email = StringField('Email', [
        validators.DataRequired(),
        validators.Email(message="Please enter a valid email address.")
    ])
    password = PasswordField('Password', [
        validators.DataRequired()
    ])

class EditUserForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired()])
    new_password_confirmed = PasswordField('New Password Confirmation', validators=[DataRequired()])
