from flask import Flask
from flask import render_template

app = Flask(__name__)

users = [
    {"id": 1, "nome": "Ana", "email": "ana@email.com", "perfil": "Admin", "status": "Ativo"},
    {"id": 2, "nome": "Bruno", "email": "bruno@email.com", "perfil": "Usuário", "status": "Ativo"},
    {"id": 3, "nome": "Carla", "email": "carla@email.com", "perfil": "Usuário", "status": "Inativo"},
    {"id": 4, "nome": "Daniel", "email": "daniel@email.com", "perfil": "Admin", "status": "Ativo"},
    {"id": 5, "nome": "Eduarda", "email": "eduarda@email.com", "perfil": "Usuário", "status": "Ativo"},
    {"id": 6, "nome": "Felipe", "email": "felipe@email.com", "perfil": "Usuário", "status": "Ativo"},
    {"id": 7, "nome": "Gabriela", "email": "gabi@email.com", "perfil": "Usuário", "status": "Inativo"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def users_page():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)