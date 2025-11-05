from flask import render_template, request, redirect, url_for, flash
from extensions import db
from models.users import User
from models.profile import Profile
from utils.uploads import save_image

def dashboard_view(current_user):
    return render_template("dashboard.html", user=current_user)

def atualizar_perfil_view(usuario):
    perfil = usuario.perfil

    if request.method == 'POST':
        telefone = request.form.get('telefone')
        instituicao = request.form.get('instituicao')
        cargo = request.form.get('cargo')
        bio = request.form.get('bio')
        foto_file = request.files.get('foto')

        foto_filename, foto_thumb = None, None
        if foto_file and foto_file.filename:
            foto_filename, foto_thumb = save_image(foto_file, user_name=usuario.nome)

        if perfil is None:
            perfil = Profile(
                user_id=usuario.id,
                telefone=telefone,
                instituicao=instituicao,
                cargo=cargo,
                bio=bio,
                foto=foto_filename,
                foto_thumb=foto_thumb
            )
            db.session.add(perfil)
        else:
            perfil.telefone = telefone
            perfil.instituicao = instituicao
            perfil.cargo = cargo
            perfil.bio = bio
            if foto_filename:
                perfil.foto = foto_filename
            if foto_thumb:
                perfil.foto_thumb = foto_thumb

        try:
            db.session.commit()
            flash('Seu perfil foi atualizado com sucesso!', 'success')
            return redirect(url_for('users.atualizar_perfil'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao salvar o perfil: {e}', 'danger')

    return render_template('users/profile.html', usuario=usuario, profile=perfil)

def list_users():
    users = User.query.all()
    return render_template("users/index.html", users=users)

def create_user():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        password = request.form.get("password")

        if User.query.filter_by(email=email).first():
            flash("Email já cadastrado.", "danger")
            return redirect(url_for("users.create_user"))

        user = User(nome=nome, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Usuário criado com sucesso.", "success")
        return redirect(url_for("users.list_users"))

    return render_template("users/form.html")

def show_user(id):
    user = User.query.get_or_404(id)
    return render_template("users/show.html", user=user)

def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == "POST":
        user.nome = request.form.get("nome")
        user.email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")
        if password:
            user.set_password(password)
        if role:
            user.role = role
        db.session.commit()
        flash("Usuário atualizado com sucesso.", "success")
        return redirect(url_for("users.show_user", id=user.id))
    return render_template("users/form.html", user=user)


def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash("Usuário excluído com sucesso.", "success")
    return redirect(url_for("users.index"))
