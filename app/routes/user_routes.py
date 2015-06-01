from flask import render_template, request, redirect, url_for
from app import nit, forms

#Login Page
@nit.route('/login')
def login():
	return 'login page'

#Register Page
@nit.route('/register', methods = ['GET', 'POST'])
def register():
	form = forms.login.SignupForm()

	if request.method == 'POST':
		return redirect(url_for('dashboard'))

	return render_template("register.html", form = form)

#User Dashboard
@nit.route('/dashboard')
def dashboard():
	return 'This is your dashboard'
