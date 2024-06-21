from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class TipoForm(FlaskForm):
     nome = StringField("nome",validators=[DataRequired()])