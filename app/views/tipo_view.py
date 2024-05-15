from app import app
from flask import render_template
from app.forms import tipo_form
from app.models import tipo_model
from app import db
@app.route("/cadtipo",methods=["POST","GET"])
def cadastrar_tipo():
      form = tipo_form.TipoForm()
      if form.validate_on_submit():
       nome = form.nome.data #capturando o conteúdo validado
       tipo = tipo_model.Tipo(nome=nome)
       try:
          #adicionar na sessão de conexão com o banco de dados
          db.session.add(tipo)
        #salvar
          db.session.commit()
       except:
         print("cliente não cadastrado")
      return render_template("tipo/form.html",form=form)