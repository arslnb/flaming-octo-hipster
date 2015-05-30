from app import nit

# MainDepartments Page
@nit.route('/departments')
def departments():
	return 'This is the departments page.'
#---------------------------------------------------------#

#Departments pagez
@nit.route('/departments/<departmentname>')
def department_page(departmentname):
	return 'This is the  ' + departmentname + 'department page.'

