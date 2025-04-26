
from flask import Flask, jsonify, request

from authentication import login_manager
from database import db
from models.user import User


app = Flask(__name__)

app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)
login_manager.init_app(app)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return jsonify({ "message": "Autenticação realizada com sucesso" })
        
    return jsonify({ "message": "Credenciais inválidas" }), 400


@app.route("/", methods=["GET"])
def health_check():
    return "Daily Diet API Health Check"


if __name__ == "__main__":
    app.run(debug=True)
