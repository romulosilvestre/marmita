from app import app, db
from flask import render_template, redirect, url_for, request
from app.forms import pedido_form
from app.models import pedido_model

@app.route("/cadpedido", methods=["POST", "GET"])
def cadastrar_pedido():
    form = pedido_form.PedidoForm()
    if form.validate_on_submit():
        data = form.data.data  # Capturando o campo 'nome' do formulário
        pedido = pedido_model.Pedido(data=data)  # Criando um novo pedido com o nome fornecido

        try:
            db.session.add(pedido)  # Adicionando o novo pedido à sessão
            db.session.commit()  # Commit para salvar no banco de dados
            return redirect(url_for('listar_pedido'))  # Redirecionando para a página de listagem de pedidos após o cadastro
        except Exception as e:
            print("Erro ao cadastrar pedido:", str(e))
            db.session.rollback()  # Em caso de erro, faz rollback da transação
            # Aqui você pode adicionar algum tratamento de erro adicional, se necessário

    return render_template("pedido/pedido.html", form=form)

@app.route("/listapedido")
def listar_pedidos():
    pedidos = pedido_model.Pedido.query.all()  # Consulta todos os pedidos cadastrados
    return render_template("pedido/lista_pedido.html", pedidos=pedidos)

