from flask import (
    Blueprint,
    jsonify,
    request
)
from flask_login import (
    current_user,
    login_required
)

from datetime import datetime
from database import db
from models.meal import Meal


bp_meal = Blueprint('meal', __name__, url_prefix="/meal")


@bp_meal.route("/", methods=["POST"])
@login_required
def register_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time") # Format: "2025-04-27 11:37:00"
    is_on_the_diet = data.get("is_on_the_diet", False)
    id_user = data.get("id_user")

    if name and date_time and id_user:
        if id_user == current_user.id:
            meal = Meal(
                name=name,
                description=description,
                date_time=datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S"),
                is_on_the_diet=is_on_the_diet,
                id_user=id_user
            )
            db.session.add(meal)
            db.session.commit()
            return jsonify({ "message": "Refeição cadastrada com sucesso" })

        return jsonify({ "message": "Operação não permitida" }), 403

    return jsonify({ "message": "Dados inválidos" }), 400


@bp_meal.route("/", methods=["GET"])
@login_required
def gel_all():
    meals = Meal.query.filter_by(id_user=current_user.id).all()

    if meals:
        return [meal.to_dict() for meal in meals]
    
    return jsonify({ "message": "Não há refeições cadastradas para este usuário" }), 404
