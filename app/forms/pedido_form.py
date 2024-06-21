from flask_wtf import FlaskForm
from wtforms import DateField, TimeField
from wtforms.validators import DataRequired, InputRequired

class PedidoForm(FlaskForm):
    data = DateField("data", validators=[DataRequired()])
    horario = TimeField("horario", validators=[InputRequired()])
