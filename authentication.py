from flask_login import LoginManager, login_user


login_manager = LoginManager()


def set_login_user(user):
    login_user(user)
