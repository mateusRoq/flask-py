from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app import routes

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(routes.bp)
    db.init_app(app)
    return app
