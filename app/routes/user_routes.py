from app import nit

#Login Page
@nit.route('/login')
def login():
	return 'login page'

#Register Page
@nit.route('/register')
def register():
	return 'register page'

#User Dashboard
@nit.route('/dashboard')
def dashboard():
	return 'This is your dashboard'
