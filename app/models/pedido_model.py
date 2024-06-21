from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import Text
from datetime import date, time
from sqlalchemy.orm import relationship

class Pedido(db.Model):
    __tablename__ = "pedido"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    data_pedido = db.Column(db.Date)
    horario = db.Column(db.Time)
    fk_formapgto_id= db.Column(db.Integer,db.ForeignKey('formapagamento.id'))
    fk_usuario_id= db.Column(db.Integer,db.ForeignKey('usuario.id'))
    fk_marmita_id= db.Column(db.Integer,db.ForeignKey('marmita.id'))   
    usuario = relationship("Usuario",back_populates="pedidos")
    marmitas = relationship("Marmita",back_populates="pedidos")
    formapgto = relationship("FormaPagamento",back_populates="pedidos")