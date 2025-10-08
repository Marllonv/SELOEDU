from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = "auth.login"  # rota para redirecionar usuários não logados
login_manager.login_message = "Por favor, faça login para acessar esta página."