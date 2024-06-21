from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired
class ItemForm(FlaskForm):
     descricao = TextAreaField("descricao",validators=[DataRequired()])