from flask import Blueprint, request
from flask_login import login_required, current_user
from views.users import (
    dashboard_view, list_users, create_user,
    show_user, edit_user, delete_user
)

users_bp = Blueprint("users", __name__)


@users_bp.route("/dashboard")
@login_required
def dashboard():
    return dashboard_view(current_user)


@users_bp.route("/list", methods=["GET"])
@login_required
def index():
    return list_users()


@users_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        return create_user()
    return create_user()


@users_bp.route("/<int:id>", methods=["GET"])
@login_required
def show(id):
    return show_user(id)


@users_bp.route("/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):
    if request.method == "POST":
        return edit_user(id)
    return edit_user(id)


@users_bp.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete(id):
    return delete_user(id)
