from flask import Flask

app = Flask(__name__)
from config import Config
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from flask_login import LoginManager
login = LoginManager(app)

from app import routes, models