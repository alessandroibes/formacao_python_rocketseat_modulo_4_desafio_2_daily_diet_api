from flask import (
    Blueprint,
    jsonify,
    request
)
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    logout_user
)

from models.user import User

bp_auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@bp_auth.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return jsonify({ "message": "Autenticação realizada com sucesso" })
        
    return jsonify({ "message": "Credenciais inválidas" }), 400


@bp_auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({ "message": "Lougout realizado com sucesso!" })
