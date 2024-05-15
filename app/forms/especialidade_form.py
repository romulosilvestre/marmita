from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired
class EspecialidadeForm(FlaskForm):
     nome = StringField("nome",validators=[DataRequired()])
   

