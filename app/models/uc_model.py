from app import db
class UnidadeCompetencia(db.Model):  
    __tablename__ = "unidadecompetencia"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    numero = db.Column(db.Integer)
    nome = db.Column(db.String(200))
    carga_horaria = db.Column(db.Integer)
    competencia_geral= db.Column(db.String(255))