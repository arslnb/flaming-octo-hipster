from app import nit
from app.models.departments import Department
from flask import render_template
# MainDepartments Page
@nit.route('/departments')
def departments():
	return 'This is the departments page.'
#---------------------------------------------------------#

#Departments pagez
@nit.route('/departments/<departmentname>')
def department_page(departmentname):
	#only one route available because database is not populated
	# http://127.0.0.1:5000/departments/ITE
	dep = Department.query.filter_by(code = departmentname).first_or_404()
	return render_template('department_base.html', dep = dep)
