from app import nit
from flask import render_template
# MainDepartments Page
@nit.route('/departments')
def departments():
	return 'This is the departments page.'
#---------------------------------------------------------#

#Departments pagez
@nit.route('/departments/<departmentname>')
def department_page(departmentname):
	return render_template('department_base.html', depname = departmentname)

