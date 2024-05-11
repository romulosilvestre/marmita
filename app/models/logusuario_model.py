from app import db

class LogUsuario(db.Model):
    __tablename__ = "log_usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hora = db.Column(db.Time)
    data = db.Column(db.Date)
    hash = db.Column(db.String(36), unique=True)
