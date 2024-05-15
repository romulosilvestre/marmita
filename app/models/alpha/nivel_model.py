from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Nivel(db.Model):
    __tablename__ = "nivel"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
