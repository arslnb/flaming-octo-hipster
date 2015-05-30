from app import nit

#Main Page
@nit.route('/')
def home():
	return 'home page'

#Blog
@nit.route('/blog')
def blog():
	return 'This is the great blog'

#Life
@nit.route('/life')
def life():
	return 'life at nit sucks.'


