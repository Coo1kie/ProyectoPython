from flask import render_template, url_for, request, redirect, flash
from app.models.Propietario import Propietario
from app import db
class PropietarioController():

    def __init__(self):
        pass

    def index1(self):
        propietarios=Propietario.query.all() #Propietario es del modelo, query-> select* from propietarios
        return render_template('propietarios/index.html', propietarios=propietarios) 
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

    def delete(self,_ci):
        propietario=Propietario.query.get(_ci)
        db.session.delete(propietario)
        db.session.commit()
        flash('El registro se eliminado con exito!!')
        return redirect(url_for('propietario_router.index'))

    def edit(self, _ci):
        propietario=Propietario.query.get(_ci) #Propietario es del modelo, get va a obtener los datos de un ci
        return render_template('propietarios/edit.html', propietario=propietario) #el segundo propietario es la variable

    def update(self, _ci):
        if request.method=='POST':
            ciV = request.form['ci']
            nombreV = request.form['nombre']
            apellidoV = request.form['apellido']
            telcelV = request.form['telcel']

            propietarioDB=Propietario.query.get(_ci)
            
            propietarioDB.ci=ciV
            propietarioDB.nombre=nombreV
            propietarioDB.apellido=apellidoV
            propietarioDB.telcel=telcelV

            db.session.commit()

            flash('El registro se actualizo con exito!!')
            return redirect(url_for('propietario_router.index'))


propietariocontroller = PropietarioController()