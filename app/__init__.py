from flask import Flask

nit = Flask(__name__)

@nit.route('/')
def test():
	return "Hello World"