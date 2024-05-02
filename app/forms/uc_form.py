from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired
class UcForm(FlaskForm):
    numero = IntegerField("numero",validators=[DataRequired()])
    nome = StringField("nome",validators=[DataRequired()])
    carga_horaria = IntegerField("carga_horaria",validators=[DataRequired()])
    competencia_geral = StringField("competencia_geral",validators=[DataRequired()])

