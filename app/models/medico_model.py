from app import db
class Medico(db.Model):  
    __tablename__ = "medico"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(200))
    fk_especialidade_id= db.Column(db.Integer,db.ForeignKey('especialidade.id'))
  