from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy.orm import relationship

class Item(db.Model):
    __tablename__ = "item"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    descricao = db.Column(db.Text)
    marmitas = relationship("Marmita",back_populates="itens")
    