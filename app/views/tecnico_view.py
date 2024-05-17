from flask import render_template, redirect, url_for
from app import app, db
from app.forms.alpha import tecnico_form
from app.models.alpha import tecnico_model

@app.route("/cadtecnico", methods=["POST", "GET"])
def cadastrar_tecnico_ok():
    form = tecnico_form.TecnicoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        nivel_id = form.nivel_id.data
        tecnico = tecnico_model.Tecnico(nome=nome, nivel_id=nivel_id)
        try:
            db.session.add(tecnico)
            db.session.commit()
            return redirect(url_for('listar_tecnicos'))
        except Exception as e:
            print(f"Erro ao cadastrar técnico:{e}")
          
    return render_template("tecnico/form_tecnico.html", form=form)

"""
@app.route("/listatecnicos")
def listar_tecnicos():
    tecnicos = Tecnico.query.all()
    return render_template("tecnico/lista_tecnico.html", tecnicos=tecnicos)

"""

