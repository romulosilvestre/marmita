from app import db
class Medico(db.Model):  
    __tablename__ = "medico"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.Integer)
    senha = db.Column(db.String(20))
    cpf = db.Column(db.String(11))
    crm = db.Column(db.Integer)
    fk_especialidade_id= db.Column(db.Integer,db.ForeignKey('especialidade.id'))
  

  