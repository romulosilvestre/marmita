from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy import Time, Date
from sqlalchemy.dialects.mysql import NCHAR

class Log(db.Model):
    __tablename__ = "log"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    #Date
    hora  = db.Column(Time)
    #Time
    data_log  = db.Column(Date)
    hash_log = db.Column(NCHAR(32))
