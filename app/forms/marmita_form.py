from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, FileField,SelectField
from wtforms.validators import DataRequired
class MarmitaForm(FlaskForm):
     nome = StringField("Nome", validators=[DataRequired()])
     foto = FileField('Foto', validators=[DataRequired()])
     peso = FloatField('Peso', validators=[DataRequired()])
     valor = FloatField('Valor', validators=[DataRequired()])
     itens = SelectField('Item', coerce=int, validators=[DataRequired()])
   