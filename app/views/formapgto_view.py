from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import formapgto_form
from app.models import formapgto_model
from app import db
@app.route("/cadformapgto",methods=["POST","GET"])
def cadastrar_formapgto():
      form = formapgto_form.FormaPgtoForm()
      if form.validate_on_submit():#confirmar o envio do formulario
         nome = form.nome.data #capturando o conteúdo validado
         formapgto = formapgto_model.FormaPagamento(nome=nome)
         try:
             #adicionar na sessão 
            db.session.add(formapgto)
            #salvar a sessão
            db.session.commit()
            if request.method == 'POST':
               return redirect(url_for('listar_formapgto'))
         except:
            print("forma de pagamento não cadastrado")
      return render_template("formapgto/form_pagamento.html",form=form)


@app.route("/listaformapgto")
def listar_formapgto():
    formaspgto = formapgto_model.FormaPagamento.query.all()  # Consulta todos os registros na tabela Nivel
    return render_template("formapgto/lista_formapgto.html", formaspgto=formaspgto)


