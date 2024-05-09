from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CursoForm(FlaskForm):
     nome = StringField("nome",validators=[DataRequired()])