from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class RecepcionistaForm(FlaskForm):
     nome = StringField("nome",validators=[DataRequired()])
     email = StringField("email",validators=[DataRequired()])
     cpf = StringField("cpf",validators=[DataRequired()])
     telefone = StringField("telefone",validators=[DataRequired()])
     senha = StringField("telefone",validators=[DataRequired()])