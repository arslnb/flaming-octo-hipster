import academic_routes, main_routes, departments_routes, updates_routes, user_routes
from app import nit

@nit.errorhandler(404)
def page_not_found(e):
	return '404', 404 