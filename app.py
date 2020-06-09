from flask import Flask,g
from config import Configuration #import configuration data

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager, current_user
from flask_bootstrap import Bootstrap

from flask_admin import Admin

app = Flask(__name__)
app.config.from_object(Configuration) #use values from our configuration object
login_manager = LoginManager(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

bootstrap = Bootstrap(app)





@app.before_request
def _before_request():
    g.user = current_user
