# routes/users.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@users_bp.route("/list")
@login_required
def list_users():
    return render_template("users.html")