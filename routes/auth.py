from flask import Blueprint
from views.auth import auth as auth_view

# 1. DEFINIÇÃO DO BLUEPRINT
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# 2. REGISTRO MANUAL DAS ROTAS
auth_bp.route("/login                 ", endpoint="login", methods=["GET", "POST"])(auth_view.login)
auth_bp.route("/logout                ", endpoint="logout", methods=["GET"])(auth_view.logout)
auth_bp.route("/forgot_password       ", endpoint="forgot_password", methods=["GET", "POST"])(auth_view.forgot_password)
auth_bp.route("/reset_password/<token>", endpoint="reset_password", methods=["GET", "POST"])(auth_view.reset_password)
