from flask import render_template, redirect, url_for
from app import app, db
from app.forms.alpha import tecnico_form
from app.models.alpha.tecnico_model import Tecnico


@app.route("/cadastrar_tecnico", methods=["POST", "GET"])
def cadastrar_tecnico():
    form = tecnico_form.TecnicoForm()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        # Aqui você pode adicionar a lógica para criar e inserir o objeto Tecnico no banco de dados
        novo_tecnico = Tecnico(nome=nome, email=email)
        db.session.add(novo_tecnico)
        db.session.commit()
        return redirect(url_for('listar_tecnicos'))
    return render_template("cadastrar_tecnico.html", form=form)
