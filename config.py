DEBUG = True
USERNAME = 'root'
PASSWORD = 'root'
SERVER = 'localhost'
DB = 'projetobase'
SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY ="minha-chave-secreta"

BABEL_DEFAULT_LOCALE = 'pt'

