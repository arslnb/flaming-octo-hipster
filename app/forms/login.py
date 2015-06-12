from flask.ext.wtf import Form 
from wtforms import TextField, validators, ValidationError, PasswordField, BooleanField, RadioField
from wtforms.validators import Required

class LoginForm(Form):
	email   = TextField('E-mail', validators = [Required()])
	password = PasswordField('Password', [validators.Required('Please enter a password.')])

class SignupForm(Form):
	name 	    = TextField('First name',[validators.Required('Please enter first name.')])
	last 	    = TextField('Last name',[validators.Required('Please enter last name.')])
	email 	    = TextField('Email',[validators.Required('Please enter email')])
	department  = TextField('Department', [validators.Required('Please enter department.')])
	year_joined = TextField('Year joined', [validators.Required('Please enter your year of joining')])
	password    = PasswordField('Password', [validators.Required('Enter a valid password')])





