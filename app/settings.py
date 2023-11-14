
from os import environ, path
from dotenv import load_dotenv
basedir = path.dirname(path.dirname(path.abspath(__file__)))
load_dotenv(path.join(basedir, ".env"))


# General Config
ENVIRONMENT = environ.get("ENVIRONMENT")
FLASK_APP = environ.get("FLASK_APP")
FLASK_DEBUG = environ.get("FLASK_DEBUG")
SECRET_KEY = environ.get("SECRET_KEY")

# Configuration for SQLite database
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False