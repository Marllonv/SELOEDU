# app.py
from flask import Flask, render_template
from models.users import db, User
from extensions import login_manager, mail
from config import Config
from routes.auth import auth_bp
from routes.users import users_bp
from routes.treinamento import treinamento_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(treinamento_bp)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()
        if not User.query.filter_by(email="admin@seloedu.com").first():
            master = User(
                nome="Admin Master",
                email="admin@seloedu.com",
                role="master"
            )
            master.set_password("123456")
            db.session.add(master)
            db.session.commit()

    @app.route("/")
    def home():
        return render_template("home.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)