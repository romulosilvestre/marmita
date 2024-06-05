from app import app
from flask import render_template
from app.forms import especialidade_form
from app.models.starc import especialidade
from app import db
@app.route("/cadespecial",methods=["POST","GET"])
def cadastrar_especialidade():
      form = especialidade_form.EspecialidadeForm()
      if form.validate_on_submit():
       nome = form.nome.data #capturando o conteúdo validado
       especial = especialidade.Especialidade(nome=nome)   
       try:
          #adicionar na sessão de conexão com o banco de dados
          db.session.add(especial)
        #salvar
          db.session.commit()
       except:
         print("especialidade não cadastrado")
      return render_template("especialidade/form.html",form=form)