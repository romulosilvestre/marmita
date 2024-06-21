from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy.orm import relationship
from sqlalchemy import Float

class Marmita(db.Model):
    __tablename__ = "marmita"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
    foto = db.Column (db.String(70))
    peso = db.Column(db.Float)
    valor = db.Column(db.Float)
    fk_item_id= db.Column(db.Integer,db.ForeignKey('item.id')) 
    itens = relationship("Item",back_populates="marmitas")
    pedidos = relationship("Pedido",back_populates="marmitas")

