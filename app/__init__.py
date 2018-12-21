from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

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


def create_app():
    app = Flask(__name__, static_folder='./static')


    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)


    from app.v1 import bp
    app.register_blueprint(bp, url_prefix='/v1')

    return app
