
from flask import Flask

from authentication import login_manager
from database import db

def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "my_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    db.init_app(app)
    login_manager.init_app(app)

    __register_blueprints(app)

    return app


def __register_blueprints(app: Flask):
    from api import bp_api
    from authentication import bp_auth

    app.register_blueprint(bp_api)
    app.register_blueprint(bp_auth)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
