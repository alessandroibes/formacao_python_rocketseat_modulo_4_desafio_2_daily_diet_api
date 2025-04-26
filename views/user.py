import bcrypt

from flask import (
    Blueprint,
    jsonify,
    request
)
from flask_login import (
    current_user,
    login_required
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
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({ "message": "Usuário cadastrado com sucesso" })
    
    return jsonify({ "message": "Dados inválidos" }), 400


@bp_user.route("/<int:id_user>", methods=["GET"])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)

    if user:
        return { "username": user.username }
    
    return jsonify({ "message": "Usuário não encontrado" }), 404


@bp_user.route("/<int:id_user>", methods=["PUT"])
@login_required
def update_user(id_user):
    data = request.json
    user = User.query.get(id_user)

    new_password = data.get("password")
    if user and new_password:
        hashed_password = bcrypt.hashpw(str.encode(new_password), bcrypt.gensalt())

        user.password = hashed_password
        db.session.commit()

        return jsonify({ "message": f"Usuário {id_user} atualizado com sucesso" })
    
    return jsonify({ "message": "Usuário não encontrado" }), 404


@bp_user.route("/<int:id_user>", methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if id_user == current_user.id:
        return jsonify({ "message": "Deleção não permitida" }), 403
    
    if user:
        db.session.delete(user)
        db.session.commit()

        return jsonify({ "message": f"Usuário {id_user} removido com sucesso" })
    
    return jsonify({ "message": "Usuário não encontrado" }), 404
