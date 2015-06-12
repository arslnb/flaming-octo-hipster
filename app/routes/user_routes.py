from flask import render_template, request, redirect, url_for
from app import nit, forms, models, db, login_manager, methods
from flask.ext.login import LoginManager, login_user, current_user, logout_user, login_required
from app.models import core

#Login Page
@nit.route('/login')
def login():
	return 'login page'

#Register Page
@nit.route('/register', methods = ['GET', 'POST'])
def register():
	form = forms.login.SignupForm()
	no_of_users = len(core.User.query.all())

	if request.method == 'POST':
		if form.name.data != "" and form.last.data != "" and form.email.data != "" and form.password.data != "":
			new_user = core.User(firstname = form.name.data, lastname = form.last.data, email = form.email.data, password = form.password.data)
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user)
			return redirect(url_for('dashboard'))
		else:
			return render_template("register.html", form = form, no_of_users = no_of_users, message = "Oops! Check the information you've entered and try again!")

	return render_template("register.html", form = form, no_of_users = no_of_users)

#User Dashboard
@login_required
@nit.route('/dashboard')
def dashboard():
	return 'This is your dashboard, %r' % (current_user.firstname)
