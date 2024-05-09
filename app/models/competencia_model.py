from app import db

class Competencia(db.Model):
    __tablename__ = "competencia"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))