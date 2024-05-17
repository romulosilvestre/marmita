from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms.alpha import nivel_form
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
          if request.method == 'POST':
           return redirect(url_for('listar_niveis'))
       except:
         print("nivel não cadastrado")
      return render_template("nivel/form_nivel.html",form=form)



@app.route("/listaniveis")
def listar_niveis():
    niveis = nivel_model.Nivel.query.all()  # Consulta todos os registros na tabela Nivel
    return render_template("nivel/lista_nivel.html", niveis=niveis)
