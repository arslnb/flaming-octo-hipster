from app import nit

#Academics route
@nit.route('/academics')
def academics():
	return 'Academic stuff goes here'

#Training and Placement route
@nit.route('/tandp')
def tandp():
	return 'This is the Training and Placement page'

#Results page
@nit.route('/results')
def results():
	return 'results go here'


