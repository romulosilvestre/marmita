#importando o flask
from flask import Flask
#importando o SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade
from flask_wtf import CSRFProtect
from flask_babel import Babel
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

babel = Babel(app)

#determinar o que vai ter no projeto
#FIXME:model
from .models import uc_model
from .models import curso_model
from .models import area_model
from .models import competencia_model
from .models import logusuario_model
from .models import tipo_model
from .models import especialidade_model
from .models import medico_model

#NOTE: Alpha InfoSystems
#FIXME:model
from .models.alpha import nivel_model
from .models.alpha import tecnico_model

#FIXME:view
from .views import nivel_view
from .views import tecnico_view

#FIXME:view
from .views import uc_view
from .views import curso_view
from .views import area_view
from .views import tipo_view
from .views import especialidade_view









