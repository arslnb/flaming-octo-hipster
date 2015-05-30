from flask.ext.wtf import Form 
from wtforms import TextField, validators, ValidationError, PasswordField, BooleanField, RadioField
from wtforms.validators import Required

class LoginForm(Form):
	email   = TextField('E-mail', validators = [Required()])
	pasword = PasswordField('Password', [validators.Required('Please enter a password.')])


class SignupForm(Form):
	name 	    = TextField('First name',[validators.Required('Please enter first name.')])
	last 	    = TextField('Last name',[validators.Required('Please enter last name.')])
	department  = TextField('Department', [validators.Required('Please enter department.')])
	year_joined = TextField('Year joined', [validators.Required('Please enter your year of joining')])
	password    = PasswordField('Password', [validators.Required('Enter a valid password')])
	user_type   = RadioField('Are you ', choices=[('student','student'),('faculty','faculty')])
	enroll		= TextField('Enrollment number',[validators.Required('Please enter your enrollment no.')])
	roll_no     = TextField('Class Roll no')





