from app import app
from flask import render_template

@app.route("/cadcurso")
def cadastrar_curso():
  return render_template("curso/cad_curso.html")