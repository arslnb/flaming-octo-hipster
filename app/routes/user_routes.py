from flask import render_template, request, redirect, url_for
from app import nit, forms, models, db, login_manager, methods
from flask.ext.login import LoginManager, login_user, current_user, logout_user, login_required
from app.models import core

#Login Page
@nit.route('/login', methods = ['GET', 'POST'])
def login():
	form = forms.login.LoginForm()
	no_of_users = len(core.User.query.all())

	if request.method == 'POST':
		if form.email.data != "" and form.password.data != "":
			user = core.User.query.filter_by(email = form.email.data).first()
			print user
			if user is not None:
				if user.check_password(form.password.data):
					login_user(user)
					return redirect(url_for('dashboard'))
				else:
					return render_template("login.html", form = form, no_of_users = no_of_users, message = "Oops! Incorrect Password. Try again!")
			else:
				return render_template("login.html", form = form, no_of_users = no_of_users, message = "Oops! You need to <a href='/register'>sign up</a> first.")
		else:
			return render_template("login.html", form = form, no_of_users = no_of_users, message = "Oops! You missed out something. Try again!")
	return render_template("login.html", form = form, no_of_users = no_of_users)

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
