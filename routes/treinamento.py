from flask import Blueprint
from flask_login import login_required, current_user
import views.treinamento as treinamento_view

treinamento_bp = Blueprint("treinamento", __name__, url_prefix="/treinamento")
treinamento_bp.add_url_rule("/", view_func=login_required(treinamento_view.listar_treinamentos), endpoint="listar", methods=["GET"])
treinamento_bp.add_url_rule("/novo",view_func=login_required(treinamento_view.novo_treinamento),endpoint="novo",methods=["GET", "POST"])
treinamento_bp.add_url_rule("/<int:id>",view_func=login_required(treinamento_view.detalhes_treinamento),endpoint="detalhes",methods=["GET"])
treinamento_bp.add_url_rule("/<int:id>/editar",view_func=login_required(treinamento_view.editar_treinamento),endpoint="editar",methods=["GET", "POST"])
treinamento_bp.add_url_rule("/<int:id>/deletar",view_func=login_required(treinamento_view.deletar_treinamento),endpoint="deletar",methods=["POST"]
)
