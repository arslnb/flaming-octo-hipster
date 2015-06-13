from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
# from flask.ext import assets
from flask.ext.login import LoginManager
import os

nit = Flask(__name__, instance_relative_config=True)
nit.config.from_pyfile('configure.py')

db = SQLAlchemy(nit)

migrate = Migrate(nit, db)
manager = Manager(nit)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(nit)
login_manager.anonymous_user.anon = True

nit.config['CSRF_ENABLED'] = True
nit.config['SECRET_KEY'] = "stay-hungry-stay-foolish"


""" 
env = assets.Environment(nit)
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'sass'),
    os.path.join(os.path.dirname(__file__), 'coffee'),
    os.path.join(os.path.dirname(__file__), 'bower_components'),
]

env.register(
    'js_home',
    assets.Bundle(
        'jquery/dist/jquery.min.js',
        'bootstrap-sass-official/assets/javascripts/bootstrap.min.js',
        output='js_home.js'
    )
)

env.register(
    'css_home',
    assets.Bundle(
        '_home.sass',
        filters='sass',
        output='css_home.css'
    )
)

"""

import routes