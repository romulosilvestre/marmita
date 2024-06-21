from flask import render_template, redirect, url_for
from app import app, db
from app.models.tipo_model import Tipo
from app.models.usuario_model import Usuario
from app.forms.tipo_form import TipoForm
from app.forms.usuario_form import UsuarioForm


from sqlalchemy.orm import joinedload


@app.route("/cadusuario", methods=["POST", "GET"])
def cadastrar_usuario():
    form = UsuarioForm()    
    # Carregar os níveis do banco de dados
    tipos = Tipo.query.all()
    # Formatar os níveis para o formato necessário para o campo de seleção
    tipo_choices = [(tipo.id, tipo.nome) for tipo in tipos]
    # Adicionar os níveis ao campo de seleção
    form.itens.choices = tipo_choices
    
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        cpf = form.cpf.data
        email  = form.email.data
        telefone = form.tele.data
        senha = form.senha.data 
        fk_tipo_id = form.itens.data        
        usuario = Usuario(nome=nome,cpf=cpf,email=email,telefone=telefone,senha=senha,fk_tipo_id=fk_tipo_id)
        try:
            db.session.add(usuario)
            db.session.commit()
            return redirect(url_for('listar_usuarios'))
        except Exception as e:
            print(f"Erro ao cadastrar usuário:{e}")
          
        return render_template("usuario/form_usuario.html", form=form)

@app.route("/listarusuarios", methods=["POST", "GET"])
def listar_usuarios():
    usuarios_com_tipo = db.session.query(Usuario).options(joinedload(Usuario.tipo)).all()
    return render_template("usuario/lista_usuario.html", usuarios=usuarios_com_tipo)
    
    

