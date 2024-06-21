from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import Text
from sqlalchemy.orm import relationship

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
    cpf = db.Column(db.String(20))
    email  = db.Column(db.String(200))
    telefone = db.Column(db.String(200))
    senha = db.Column(db.String(200))
    fk_tipo_id= db.Column(db.Integer,db.ForeignKey('tipo.id'))
    tipo = relationship("Tipo",back_populates="usuarios")
    pedidos = relationship("Pedido",back_populates="usuario")

    def __init__(self, nome, cpf, email, telefone, senha, fk_tipo_id):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.fk_tipo_id = fk_tipo_id