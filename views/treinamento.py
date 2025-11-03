from flask import render_template, request, redirect, url_for, flash
from models.treinamento import Treinamento
from models.users import db
from flask_login import current_user
from datetime import datetime

def listar_treinamentos():
    treinamentos = Treinamento.query.order_by(Treinamento.data_inicio.desc()).all()
    return render_template("treinamento/listar.html", treinamentos=treinamentos)

def novo_treinamento():
    if current_user.role != "coordenador":
        return "Acesso negado", 403

    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        data_inicio_str = request.form.get("data_inicio")
        data_fim_str = request.form.get("data_fim")

        try:
            data_inicio = datetime.strptime(data_inicio_str, "%Y-%m-%d").date()
            data_fim = datetime.strptime(data_fim_str, "%Y-%m-%d").date()
        except ValueError:
            flash("Formato de data inválido.", "danger")
            return render_template("treinamento/novo.html")

        treinamento = Treinamento(
            titulo=titulo,
            descricao=descricao,
            data_inicio=data_inicio,
            data_fim=data_fim
        )
        db.session.add(treinamento)
        db.session.commit()
        flash("Treinamento criado com sucesso!", "success")
        return redirect(url_for("treinamento.listar"))

    return render_template("treinamento/novo.html")

def detalhes_treinamento(id):
    treinamento = Treinamento.query.get_or_404(id)
    return render_template("treinamento/detalhes.html", treinamento=treinamento)

def editar_treinamento(id):
    treinamento = Treinamento.query.get_or_404(id)

    if current_user.role != "coordenador":
        return "Acesso negado: apenas coordenadores podem editar", 403

    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        data_inicio = request.form.get("data_inicio")
        data_fim = request.form.get("data_fim")

        if not titulo or not data_inicio or not data_fim:
            flash("Título, Data Início e Data Fim são obrigatórios.", "danger")
            return render_template("treinamento/editar.html", treinamento=treinamento)

        treinamento.titulo = titulo
        treinamento.descricao = descricao
        treinamento.data_inicio = data_inicio
        treinamento.data_fim = data_fim
        db.session.commit()
        flash("Treinamento atualizado com sucesso!", "success")
        return redirect(url_for("treinamento.detalhes", id=id))

    return render_template("treinamento/editar.html", treinamento=treinamento)

def deletar_treinamento(id):
    if current_user.role != "coordenador":
        return "Acesso negado: apenas coordenadores podem deletar", 403

    treinamento = Treinamento.query.get_or_404(id)
    db.session.delete(treinamento)
    db.session.commit()
    flash("Treinamento deletado com sucesso!", "success")
    return redirect(url_for("treinamento.listar"))
