import logging.config
import os
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from app.config import config
from app.models.base import db

Config = config["default"]

base_dir = os.path.abspath(os.path.dirname(__file__))
static_path = os.path.join(base_dir, "static")


migrate = Migrate()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["1000/minute"],
    headers_enabled=True  # X-RateLimit写入响应头。
)


def register_plug(app):
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()


def register_blueprint(app):
    from app.api_v1 import bp
    app.register_blueprint(bp, url_prefix='/api/v1')


def create_app(config_class=Config):
    # logging.config.fileConfig(os.path.join(os.path.abspath(os.path.dirname(__file__)), "logging.conf"))
    app = Flask(__name__, static_folder='./static')
    app.config.from_object(config_class)


    limiter.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    register_blueprint(app)

    # register_plug(app)

    return app
