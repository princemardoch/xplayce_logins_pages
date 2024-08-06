import secrets

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    app.config['SECRET_KEY'] = secrets.token_urlsafe(30)
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    from .auth.authr import auth
    from .user.userr import user

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(user, url_prefix='/')

    return app