from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext import assets
import os
import sass

nit = Flask(__name__, instance_relative_config=True)
nit.config.from_pyfile('configure.py')

db = SQLAlchemy(nit)


env = assets.Environment(nit)
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'bower_components'),
    os.path.join(os.path.dirname(__file__), 'sass'),
    os.path.join(os.path.dirname(__file__), 'coffee'),
]

env.register(
    'js_home',
    assets.Bundle(
        'jquery/dist/jquery.min.js',
        'bootstrap-sass-official/assets/javascripts/bootstrap.min.js',
        output='js_home.js'
    )
)

# env.register(
#     'css_home',
#     assets.Bundle(
#         '_home.sass',
#         filters='scss,sass',
#         output='css_home.css'
#     )
# )
sass.foo()
import routes