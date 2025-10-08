from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.users import db, User

users_bp = Blueprint("users", __name__)

@users_bp.route("/users")
@login_required
def index():
    users = User.query.all()
    return render_template("users/index.html", users=users)

@users_bp.route("/users/new", methods=["GET", "POST"])
@login_required
def new():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        password = request.form.get("password")
        if User.query.filter_by(email=email).first():
            flash("Email já cadastrado.", "danger")
            return redirect(url_for("users.new"))
        user = User(nome=nome, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Usuário criado com sucesso.", "success")
        return redirect(url_for("users.index"))
    return render_template("users/form.html")

@users_bp.route("/users/<int:id>")
@login_required
def show(id):
    user = User.query.get_or_404(id)
    return render_template("users/show.html", user=user)

@users_bp.route("/users/<int:id>/edit", methods=["GET", "POST"])
@login_required
def edit(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.nome = request.form.get("nome")
        user.email = request.form.get("email")
        password = request.form.get("password")
        if password:
            user.set_password(password)
        db.session.commit()
        flash("Usuário atualizado com sucesso.", "success")
        return redirect(url_for("users.show", id=user.id))
    return render_template("users/form.html", user=user)

@users_bp.route("/users/<int:id>/delete", methods=["POST"])
@login_required
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuário excluído com sucesso.", "success")
    return redirect(url_for("users.index"))
