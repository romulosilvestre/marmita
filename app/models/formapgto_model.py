from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy.orm import relationship

class FormaPagamento(db.Model):
    __tablename__ = "formapagamento"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(200))
    pedidos = relationship("Pedido",back_populates="formapgto")