from app import app
from flask import render_template,redirect,url_for,request #renderização
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
          #adicionar na sessão 
          db.session.add(tipo)
          #salvar a sessão
          db.session.commit()
          if request.method == 'POST':
           return redirect(url_for('listar_tipos'))
       except:
         print("tipo não cadastrado")
      return render_template("tipo/form_tipo.html",form=form,editar=False)



@app.route("/listatipos")
def listar_tipos():
    tipos = tipo_model.Tipo.query.all()  # Consulta todos os registros na tabela Nivel
    return render_template("tipo/lista_tipo.html", tipos=tipos)

@app.route("/listatipo/<int:id>")
def listar_tipo(id):
    tipo = tipo_model.Tipo.query.filter_by(id=id).first()  # Consulta todos os registros na tabela Nivel
    return render_template("tipo/lista_tipo_id.html",tipo=tipo)

@app.route("/editartipo/<int:id>",methods=["POST","GET"])
def editar_tipo(id):
   tipo = tipo_model.Tipo.query.filter_by(id=id).first() 
   # vamos agora criar o nosso nível de formulário
   form = tipo_form.TipoForm(obj=tipo)
   # verificar se todos os dados estão ok
   if form.validate_on_submit():
      nome = form.nome.data
      tipo.nome = nome

      try:
          db.session.commit()
          return redirect(url_for("listar_tipos"))
      except:
          print("o cliente não foi editado")
         
   return render_template("tipo/form_tipo.html",form=form,editar=True)

@app.route("/removertipo/<int:id>",methods=["POST","GET"])
def remover_tipo(id):
     tipo = tipo_model.Tipo.query.filter_by(id=id).first() 
     # vamos indicar que o usuário clicou no botão remover
     # importe request
     if request.method == "POST":
        try:
             db.session.delete(tipo)
             db.session.commit()
             return redirect(url_for("listar_tipo"))
        except:
             print("erro ao deletar tipo")
     return render_template("tipo/remover_tipo.html",tipo=tipo)
   