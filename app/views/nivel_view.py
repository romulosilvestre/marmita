from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import nivel_form
from app.models import nivel_model
from app import db
@app.route("/",methods=["POST","GET"])
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
      return render_template("nivel/form_nivel.html",form=form,editar=False)



@app.route("/listaniveis")
def listar_niveis():
    niveis = nivel_model.Nivel.query.all()  # Consulta todos os registros na tabela Nivel
    return render_template("nivel/lista_nivel.html", niveis=niveis)

@app.route("/listanivel/<int:id>")
def listar_nivel(id):
    nivel = nivel_model.Nivel.query.filter_by(id=id).first()  # Consulta todos os registros na tabela Nivel
    return render_template("nivel/lista_nivel_id.html",nivel=nivel)

@app.route("/editarnivel/<int:id>",methods=["POST","GET"])
def editar_nivel(id):
   nivel = nivel_model.Nivel.query.filter_by(id=id).first() 
   # vamos agora criar o nosso nível de formulário
   form = nivel_form.NivelForm(obj=nivel)
   # verificar se todos os dados estão ok
   if form.validate_on_submit():
      nome = form.nome.data
      nivel.nome = nome

      try:
          db.session.commit()
          return redirect(url_for("listar_niveis"))
      except:
          print("o cliente não foi editado")
         
   return render_template("nivel/form_nivel.html",form=form,editar=True)

@app.route("/removernivel/<int:id>",methods=["POST","GET"])
def remover_nivel(id):
     nivel = nivel_model.Nivel.query.filter_by(id=id).first() 
     # vamos indicar que o usuário clicou no botão remover
     # importe request
     if request.method == "POST":
        try:
             db.session.delete(nivel)
             db.session.commit()
             return redirect(url_for("listar_niveis"))
        except:
             print("erro ao deletar nível")
     return render_template("nivel/remover_nivel.html",nivel=nivel)
   