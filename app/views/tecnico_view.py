from flask import render_template, redirect, url_for
from app import app, db
from app.forms.alpha import tecnico_form
from app.models.alpha import tecnico_model
from app.models.alpha.tecnico_model import Tecnico
from app.models.alpha.nivel_model import Nivel
from app.models.alpha import nivel_model
from sqlalchemy.orm import joinedload


@app.route("/cadtecnico", methods=["POST", "GET"])
def cadastrar_tecnico_ok():
    form = tecnico_form.TecnicoForm()
    
    # Carregar os níveis do banco de dados
    niveis = nivel_model.Nivel.query.all()
    # Formatar os níveis para o formato necessário para o campo de seleção
    nivel_choices = [(nivel.id, nivel.nome) for nivel in niveis]
    # Adicionar os níveis ao campo de seleção
    form.nivel_id.choices = nivel_choices
    
    if form.validate_on_submit():
        nome = form.nome.data
        nivel_id = form.nivel_id.data
        email = form.email.data
        tecnico = tecnico_model.Tecnico(nome=nome,email=email,fk_nivel_id=nivel_id)
        try:
            db.session.add(tecnico)
            db.session.commit()
            return redirect(url_for('listar_tecnicos'))
        except Exception as e:
            print(f"Erro ao cadastrar técnico:{e}")
          
    return render_template("tecnico/form_tecnico.html", form=form)

@app.route("/listartecnicos", methods=["POST", "GET"])
def listar_tecnicos():
    #tecnicos = tecnico_model.Tecnico.query.all()  # Consulta todos os registros na tabela Nivel
    tecnicos_com_nivel = db.session.query(Tecnico).options(joinedload(Tecnico.nivel)).all()
    return render_template("tecnico/lista_tecnico.html", tecnicos=tecnicos_com_nivel)
    
    

