import academic_routes, main_routes, departments_routes, updates_routes, user_routes

@nit.errorhandler(404)
def page_not_found(e):
	retrun '404' 404 