from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile("settings.py")
db = SQLAlchemy(app)

migrate = Migrate(app, db)

__import__('app.models')
__import__('app.blueprints')