from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from app import db

class Prontuario(db.Model):
    __tablename__ = 'prontu'
    
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer,db.ForeignKey('pacie.id'),unique=True)
    historico = db.Column(db.String(200))
    
    # Relacionamento um-para-um com Paciente
    paciente = relationship("Pacie", back_populates="prontu")