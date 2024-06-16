from database.db import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    idusuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(30), nullable=False)
    idperfil = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'idusuario': self.idusuario,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'senha': self.senha,
            'idperfil': self.idperfil,
            'tabela': 'usuarios'
        }
