from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class EditUserForm(FlaskForm):
    first_name = StringField('First name', validators=[validators.DataRequired()])
    last_name = StringField('Last name', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired()])
    new_password = PasswordField(
        'New Password', 
        validators=[
            validators.EqualTo('new_password_confirmed',message='Passwords must match')
        ])
    new_password_confirmed = PasswordField('New Password Confirmation', validators=[])
    