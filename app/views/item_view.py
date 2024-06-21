from flask import render_template, redirect, url_for, request
from app import app, db
from app.forms import item_form
from app.models import item_model

@app.route("/caditem", methods=["POST", "GET"])
def cadastrar_item():
    form = item_form.ItemForm()
    if form.validate_on_submit():
        descricao = form.descricao.data
        item = item_model.Item(descricao=descricao)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect(url_for('listar_itens'))
        except Exception as e:
            print("Erro ao cadastrar item:", e)
            db.session.rollback()  # Rollback da transação em caso de erro
    return render_template("item/item.html", form=form)

@app.route("/listaitem")
def listar_itens():
    itens = item_model.Item.query.all()
    return render_template("item/lista_item.html", itens=itens)
