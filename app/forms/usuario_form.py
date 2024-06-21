from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,PasswordField
from wtforms.validators import DataRequired, Email

class UsuarioForm(FlaskForm):
   nome = StringField('Nome', validators=[DataRequired()])
   email = StringField('Email', validators=[DataRequired()])
   cpf = StringField('CPF', validators=[DataRequired()])  # Adicionado campo CPF
   telefone = StringField('Telefone', validators=[DataRequired()])  # Adicionado campo Telefone
   senha = PasswordField('Senha', validators=[DataRequired()])  # Adicionado campo Senha
   tipo_id = SelectField('Tipo', coerce=int, validators=[DataRequired()])