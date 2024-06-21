from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms import marmita_form
from app.models import marmita_model
from app.forms.pedido_form import PedidoForm
from app.models.item_model import Item
from app import db
from werkzeug.utils import secure_filename
import os

@app.route("/cadmarmita",methods=["POST","GET"])
def cadastrar_marmita():
      form = marmita_form.MarmitaForm()
      # Carregar os níveis do banco de dados
      itens = Item.query.all()
      # Formatar os níveis para o formato necessário para o campo de seleção
      itens_choices = [(item.id, item.descricao) for item in itens]
      # Adicionar os níveis ao campo de seleção
      form.itens.choices = itens_choices
    
      if form.validate_on_submit():#confirmar o envio do formulario
         nome = form.nome.data
         foto = "static/foto/marmita.png"
         peso = form.peso.data
         valor = form.valor.data #capturando o conteúdo validado
               
         fk_item_id = form.itens.data
         marmita = marmita_model.Marmita(nome=nome,foto=foto,peso=peso,valor=valor,fk_item_id=fk_item_id)
    
         try:
             #adicionar na sessão 
            db.session.add(marmita)
            #salvar a sessão
            db.session.commit()
            if request.method == 'POST':
               return redirect(url_for('listar_marmita'))
         except:
            print("Marmita não encontrada")
      return render_template("marmita/marmita.html",form=form)


@app.route("/listamarmita")
def listar_marmita():
    marmitas = marmita_model.Marmita.query.all()  # Consulta todos os registros na tabela Nivel
    return render_template("marmita/marmita.html", marmitas=marmitas)