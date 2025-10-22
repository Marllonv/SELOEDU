from flask import Blueprint
from views.auth import login as login_view, logout as logout_view, 

# 1. DEFINIÇÃO DO BLUEPRINT
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# 2. REGISTRO MANUAL DAS ROTAS

# Rota de Login: /auth/login
auth_bp.route("/login", endpoint="login", methods=["GET", "POST"])(login_view)

# Rota de Logout: /auth/logout
auth_bp.route("/logout", endpoint="logout", methods=["GET"])(logout_view)

# Rota de Recovery: /auth/recovery
auth_bp.route("/forgot_password", endpoint="forgot_password", methods=["GET", "POST"])(recovery_view)

# Rota de Reset Password: /auth/reset_password
auth_bp.route("/reset_password", endpoint="reset_password", methods=["GET", "POST"])(recovery_view)
