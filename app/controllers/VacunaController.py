from flask import render_template, url_for
class VacunaController():
    def __init__(self):
        pass

    def index1(self):
        return render_template('vacunas/index.html') 
    def create(self):
        return render_template('vacunas/create.html') #rederizar vista
vacunacontroller = VacunaController()