from app import nit
#new updates
@nit.route('/updates')
def updates():
	return 'This is the updates page.'
#Events
@nit.route('/events')
def updates():
	return 'This is the events page.'

#upcoming activities
@nit.route('/activities')
def activities():
	return 'This is the activities page'

#publications
@nit.route('/publications')
def publications():
	return 'publications go here'
