from app import app
from flask import render_template #renderização
from app.forms import nivel_form
from app.models.alpha import nivel_model
from app import db
@app.route("/cadnivel",methods=["POST","GET"])
def cadastrar_nivel():
      form = nivel_form.NivelForm()
      if form.validate_on_submit():
       nome = form.nome.data #capturando o conteúdo validado
       nivel = nivel_model.Nivel(nome=nome)
       try:
          #adicionar na sessão 
          db.session.add(nivel)
          #salvar a sessão
          db.session.commit()
       except:
         print("nivel não cadastrado")
      return render_template("nivel/form_nivel.html",form=form)