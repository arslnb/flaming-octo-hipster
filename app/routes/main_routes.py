from app import nit
from flask import render_template

current_user = "Arsalasn"

#Main Page
@nit.route('/')
def home():
	if current_user is None:
		return render_template("home.html")
	else:
		return render_template("dashboard.html")

#Blog
@nit.route('/blog')
def blog():
	return 'This is the great blog'

#Life
@nit.route('/life')
def life():
	return 'life at nit sucks.'


