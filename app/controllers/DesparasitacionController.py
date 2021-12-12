from flask import render_template, url_for
class DesparasitacionController():
    def __init__(self):
        pass

    def index1(self):
        return render_template('desparasitaciones/index.html') 
    
    def create(self):
        return render_template('desparasitaciones/create.html') #rederizar vista
desparasitacioncontroller = DesparasitacionController()