from flask.ext.wtf import Form 
from wtforms import TextField, validators, ValidationError, PasswordField, FieldField, BooleanField, RadioField
from wtforms.validators import Required

class LoginForm(Form):
	email = TextField('E-mail', validators = [Required()])
	pasword = PasswordField('Password', [validators.Required('Please enter a password.')])


class SignupForm(Form):
	name = TextField('First name',[validators.Required('Please enter first name.')])
