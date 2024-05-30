#mostrar os erros em tempo real
DEBUG = True
#usuário
USERNAME = 'root'
#senha
PASSWORD = 'root'
#servidor
SERVER = 'localhost'
#nome do banco de dados
#create database ....
# SQLAlchemy

DB = 'alphateste'
#connection string
SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
#modificação
SQLALCHEMY_TRACK_MODIFICATIONS = True
#chave secreta - hash  (chave criptografada)
#entrar em qualquer site que gere hash - colocar o hash
#publicar.
SECRET_KEY ="8a4dbb9594173ae2747f9704468a89bd"

#português
BABEL_DEFAULT_LOCALE = 'pt'

