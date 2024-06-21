from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy.orm import relationship

class Tipo(db.Model):
    __tablename__ = "tipo"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
    usuarios = relationship("Usuario",back_populates="tipo")
