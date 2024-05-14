from app import app
from flask import render_template

@app.route('/cadtipo')
def cadastrar_tipo():
      return render_template("tipo/cad_tipo.html")