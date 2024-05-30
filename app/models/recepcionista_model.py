from app import db
class Recepcionista(db.Model):  
    __tablename__ = "recepcionista"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(80))
    telefone = db.Column(db.String(40))
    cpf = db.Column(db.String(80))
    email = db.Column(db.String(80))
    senha = db.Column(db.String(80))