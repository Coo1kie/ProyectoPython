from flask import render_template, url_for
class ConsultaController():
    def __init__(self):
        pass

    def index1(self):
        return render_template('consultas/index.html') 
    def create(self):
        return render_template('consultas/create.html') #rederizar vista
consultacontroller = ConsultaController()