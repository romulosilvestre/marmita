#importando o flask
from flask import Flask
#importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade
from flask_wtf import CSRFProtect

#criando o aplicativo
app = Flask(__name__)
#puxando o arquivo config.py
app.config.from_object('config')
#criando um objeto db da classe SQLAlchemy
db = SQLAlchemy(app)
#criar uma variável migrate e passar a instância da aplicação e do db
migrate = Migrate(app,db)
csrf = CSRFProtect(app)
csrf.init_app(app)


#FIXME:model
from app.models import tipo_model
from app.models import usuario_model
from app.models import formapgto_model
from app.models import pedido_model
from app.models import item_model
from app.models import marmita_model

#FIXME:view
from .views import tipo_view
from .views import usuario_view
from .views import formapgto_view
from .views import item_view
from .views import marmita_view
from .views import pedido_view











