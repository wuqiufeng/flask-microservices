from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


def create_app():
    app = Flask(__name__, static_folder='./static')
    Limiter(key_func=get_remote_address, headers_enabled=True, default_limits=["1000/minute"]).init_app(app)
    from app.onecity_v1 import bp
    app.register_blueprint(bp, url_prefix='/onecity/v1')

    return app