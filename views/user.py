from flask import (
    Blueprint,
    jsonify,
    request
)

from database import db
from models.user import User

bp_user = Blueprint('user', __name__, url_prefix="/user")


@bp_user.route("/", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify({ "message": "Usuário cadastrado com sucesso" })
    
    return jsonify({ "message": "Dados inválidos" }), 400
