from app import nit, db
from werkzeug import generate_password_hash, check_password_hash
import datetime, hashlib, uuid

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String())
	lastname = db.Column(db.String())
	email = db.Column(db.String(), unique = True)
	pwdhash = db.Column(db.Text(255))
	salt = db.Column(db.Text(255))
	resethash = db.Column(db.Text(255))

	#notification = db.relationship('Notification', backref = 'user', lazy = 'dynamic')
	faculty = db.relationship('Faculty', backref = 'user', lazy = 'dynamic')
	student = db.relationship('Student', backref = 'user', lazy = 'dynamic')

	def __init__(self, firstname, lastname, email, password):
		self.email = email
		self.firstname = firstname
		self.lastname = lastname
		self.salt = uuid.uuid4().hex
		self.set_password(password + self.salt)
		self.resethash = self.generate_regen_salt()

	def set_password(self, password):
		self.pwdhash = generate_password_hash(password)

	def generate_regen_salt(self):
		return uuid.uuid4().hex

	def check_password(self, password):
		return check_password_hash(self.pwdhash, password + self.salt)

	def makeFaculty(self):
		pass

	def makeStudent(self):
		pass

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def is_active(self):
		return True

	def __repr__(self):
		return '<User %r>' % (self.email)

class Faculty(db.Model):
	__tablename__ = 'faculty'
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	department = db.Column(db.String(3))
	qualification = db.Column(db.Text())
	year_joined = db.Column(db.Integer)

	def __repr__(self):
		return '<Faculty %r>' % (self.department)


class Student(db.Model):
	__tablename__ = 'student'
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	department = db.Column(db.String(3))
	year_of_enroll = db.Column(db.String(2))
	class_roll = db.Column(db.Integer)

	def __repr__(self):
		return '<Faculty %r>' % (self.department)



