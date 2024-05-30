from app import db

class Pagamento(db.Model):
    __tablename__ = "pagamento"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    descricao  = db.Column(db.String(200))