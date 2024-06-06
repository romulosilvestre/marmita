from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from app import db


class Pacie(db.Model):
    __tablename__ = 'pacie'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    
    # Relacionamento um-para-um com Prontuario
    prontuario = relationship("Prontuario", back_populates="pacie", uselist=False,cascade="all, delete-orphan")