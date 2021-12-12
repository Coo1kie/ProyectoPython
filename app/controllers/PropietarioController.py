from flask import render_template, url_for, request, redirect, flash
from app.models.Propietario import Propietario
from app import db
class PropietarioController():

    def __init__(self):
        pass

    def index1(self):
        return render_template('propietarios/index.html') 
    def create(self):
        return render_template('propietarios/create.html') #rederizar vista

    def store(self):
        if request.method=='POST':
            ci = request.form['ci']
            nombre = request.form['nombre']
            apellido = request.form['apellido']
            telcel = request.form['telcel']

            propietarioadd=Propietario(ci=ci, nombre=nombre, apellido=apellido, telcel=telcel)

            db.session.add(propietarioadd)
            db.session.commit()

            flash('El registro se realizo con exito!!')
            return redirect(url_for('propietario_router.index'))
        
propietariocontroller = PropietarioController()