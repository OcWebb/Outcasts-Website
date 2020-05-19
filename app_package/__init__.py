from flask import Flask
from .extensions import db

app = Flask(__name__)

app.config.from_pyfile('settings.py')

db.init_app(app)


from app_package import routes
