from app import nit, db

class Department(db.Model):
	__tablename__ = "department"
	"""docstring for Department"""
	id 	 = db.Column(db.Integer(), primary_key = False)
	code = db.Column(db.String(3), primary_key = True)
	name = db.Column(db.String(80))
	description = db.Column(db.String())

	#one to many relation with Student and Faculty
	students = db.relationship('Student', backref = 'department') 
	faculty  = db.relationship('Faculty', backref = 'department')


	def __init__(self, code,name,description):
		self.code = code
		self.name = name
		self.description = description

	def __repr__(self):
		return '<Department %r' % self.name		