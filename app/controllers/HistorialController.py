from flask import render_template, url_for
class HistorialController():
    def __init__(self):
        pass

    def index1(self):
        return render_template('historiales/index.html') 
    def create(self):
        return render_template('historiales/create.html') #rederizar vista
historialcontroller = HistorialController()