# app/__init__.py
from flask import Flask
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from .config import config

bcrypt = Bcrypt()
mongo = None

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    global mongo
    mongo = MongoClient(app.config["MONGO_URI"]).get_database()
    bcrypt.init_app(app)
    from .routes.user_routes import user_map
    app.register_blueprint(user_map, url_prefix="/api")
    return app
