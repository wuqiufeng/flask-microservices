import logging.config
import os
from dotenv import load_dotenv

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import config

SETTINGS = config["default"]

base_dir = os.path.abspath(os.path.dirname(__file__))
static_path = os.path.join(base_dir, "static")


db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["1000/minute"],
    headers_enabled=True  # X-RateLimit写入响应头。
)


def register_plug(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprint(app):
    from app.v1 import bp
    app.register_blueprint(bp, url_prefix='/pushmsg/v1')


def create_app():
    # logging.config.fileConfig(os.path.join(os.path.abspath(os.path.dirname(__file__)), "logging.conf"))
    app = Flask(__name__, static_folder='./static')
    UPLOAD_FOLDER = os.path.join(base_dir, "uploads")
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    register_blueprint(app)

    return app
