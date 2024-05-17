from flask_wtf import FlaskForm
from wtforms import StringField,SelectField
from wtforms.validators import DataRequired, Email

class TecnicoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    nivel_id = SelectField('Nivel', coerce=int, validators=[DataRequired()])