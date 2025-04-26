from flask import Blueprint


bp_api = Blueprint('api', __name__, url_prefix="/")


@bp_api.route("/", methods=["GET"])
def health_check():
    return "Daily Diet API Health Check"
