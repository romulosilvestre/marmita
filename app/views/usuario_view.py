from flask import render_template, redirect, url_for
from app import app, db
from app.models.nivel_model import Nivel
from app.models.usuario_model import Usuario
from app.forms.nivel_form import NivelForm
from app.forms.usuario_form import UsuarioForm


from sqlalchemy.orm import joinedload


@app.route("/cadusuario", methods=["POST", "GET"])
def cadastrar_usuario():
    form = UsuarioForm()
    
    # Carregar os níveis do banco de dados
    niveis = Nivel.query.all()
    # Formatar os níveis para o formato necessário para o campo de seleção
    nivel_choices = [(nivel.id, nivel.nome) for nivel in niveis]
    # Adicionar os níveis ao campo de seleção
    form.nivel_id.choices = nivel_choices
    
    if form.validate_on_submit():
        nome = form.nome.data
        nivel_id = form.nivel_id.data
        email = form.email.data
        tecnico = Usuario(nome=nome,email=email,fk_nivel_id=nivel_id)
        try:
            db.session.add(tecnico)
            db.session.commit()
            return redirect(url_for('listar_usuarios'))
        except Exception as e:
            print(f"Erro ao cadastrar usuário:{e}")
          
    return render_template("usuario/form_usuario.html", form=form)

@app.route("/listarusuarios", methods=["POST", "GET"])
def listar_usuarios():
    #tecnicos = tecnico_model.Tecnico.query.all()  # Consulta todos os registros na tabela Nivel
    usuarios_com_nivel = db.session.query(Usuario).options(joinedload(Usuario.nivel)).all()
    return render_template("usuario/lista_usuario.html", usuarios=usuarios_com_nivel)
    
    

