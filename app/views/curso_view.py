from app import app
from flask import render_template
from app.forms import curso_form
from app import db
from app.models import curso_model

@app.route("/cadcurso",methods=["POST","GET"])
def cadastrar_curso():
  form = curso_form.CursoForm()
  #verificar se as informações são validas
  #o que ele digitou estão de acordo com nossas regras
  if form.validate_on_submit():
     #todos os dados estão de acordo
     nome = form.nome.data #capturando o conteúdo validado
  
     #vamos criar um objeto cliente
     curso = curso_model.Curso(nome=nome)
     #chamar db (instância da conexão com nosso banco)
     try:
        #adicionar na sessão de conexão com o banco de dados
        db.session.add(curso)
        #salvar
        db.session.commit()
     except:
        print("cliente não cadastrado")
  return render_template("curso/form.html",form=form)


@app.route("/listacurso",methods=["GET"])
def listar_curso():
     return render_template("curso/lista_curso.html")