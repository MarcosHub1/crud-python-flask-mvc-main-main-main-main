from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)  # Armazena hash seguro
    estado = db.Column(db.String(100), nullable=False)
    cidade = db.Column(db.String(100), nullable=True)
    telefone = db.Column(db.String(100), nullable=False)
    foto_perfil = db.Column(db.String(200), nullable=True)

    pets = db.relationship('Pet', backref='dono', lazy=True)

    def set_password(self, senha):
        # Gera hash seguro compatível com versões recentes do Werkzeug
        self.senha = generate_password_hash(senha, method="pbkdf2:sha256")

    def check_password(self, senha):
        return check_password_hash(self.senha, senha)



class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    cor = db.Column(db.String(50), nullable=True)  # ← novo campo
    idade = db.Column(db.String(20), nullable=True)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="adocao")
    imagem = db.Column(db.String(200), nullable=True)
    contato = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # FK: cada pet pertence a um usuário
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Pet {self.nome}>'
