from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela

class Tecnico(db.Model):
    __tablename__ = "tecnico"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
    email  = db.Column(db.String(200))
    fk_nivel_id= db.Column(db.Integer,db.ForeignKey('nivel.id'))