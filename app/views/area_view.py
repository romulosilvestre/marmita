from app import app
from flask import render_template

@app.route("/cadarea")
def cadastrar_area():
    return render_template("area/cad_area.html")