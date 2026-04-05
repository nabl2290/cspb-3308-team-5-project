from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class EditUserForm(FlaskForm):
    first_name = StringField('First name', validators=[validators.DataRequired()])
    last_name = StringField('Last name', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired()])
    password = PasswordField(
        'New Password', 
        validators=[
            validators.EqualTo('password_confirmed',message='Passwords must match')
        ])
    password_confirmed = PasswordField('New Password Confirmation', validators=[])
    