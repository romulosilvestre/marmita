from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class NivelForm(FlaskForm):
     nome = StringField("nome",validators=[DataRequired()])