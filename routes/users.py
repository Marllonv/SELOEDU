from flask import Blueprint
from flask_login import login_required, current_user
from views.users import (
    dashboard_view, list_users, create_user,
    show_user, edit_user, delete_user, atualizar_perfil_view
)

users_bp = Blueprint("users", __name__)

def dashboard():
    return dashboard_view(current_user)

def atualizar_perfil():
    return atualizar_perfil_view(current_user)

users_bp.add_url_rule("/dashboard", view_func=login_required(dashboard))
users_bp.add_url_rule("/perfil", view_func=login_required(atualizar_perfil), methods=["GET", "POST"])
users_bp.add_url_rule("/list", view_func=login_required(list_users))
users_bp.add_url_rule("/new", view_func=login_required(create_user), methods=["GET", "POST"])
users_bp.add_url_rule("/<int:id>", view_func=login_required(show_user), methods=["GET"])
users_bp.add_url_rule("/<int:id>/edit", view_func=login_required(edit_user), methods=["GET", "POST"])
users_bp.add_url_rule("/<int:id>/delete", view_func=login_required(delete_user), methods=["POST"])
