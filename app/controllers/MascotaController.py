from flask import render_template, url_for, request, redirect, flash
from app.models.Mascota import Mascota
from app.models.Propietario import Propietario
from app import db
class MascotaController():
    def __init__(self):
        pass

    def index1(self):
        mascotas=Mascota.query.join(Propietario).filter().all()
        return render_template('mascotas/index.html', mascotas=mascotas) 

    def create(self):
        propietarios=Propietario.query.all()
        
        return render_template('mascotas/create.html',propietarios=propietarios) #rederizar vista
    
    def store(self):
        if request.method == 'POST':
            name = request.form['name']
            especie = request.form['especie']
            raza = request.form['raza']
            genero=request.form['genero']
            color=request.form['color']
            fechanac = request.values['fechanac']
            esterilizacion = request.values['esterilizacion']
            propietario_id = request.values['propietario_id']
            
            mascotaadd = Mascota(name=name, especie=especie, raza=raza,
                         genero=genero,color=color,fechanac=fechanac, esterilizacion=esterilizacion,  propietario_id=propietario_id)
            db.session.add(mascotaadd)
            db.session.commit()
            flash('Mascota creado exitosamente')
            return redirect(url_for('mascota_router.index'))
    
    def delete(self, _idm):
        mascota = Mascota.query.get(_idm)
        db.session.delete(mascota)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('mascota_router.index'))


    def edit(self, _idm):
        mascota = Mascota.query.get(_idm)
        propietarios = Propietario.query.all()
        return render_template('mascotas/edit.html', mascota=mascota, propietarios=propietarios)

    def update(self, _idm):
        if request.method == 'POST':
            name = request.form['name']
            especie = request.form['especie']
            raza = request.form['raza']
            genero=request.form['genero']
            color=request.form['color']
            fechanac = request.values['fechanac']
            esterilizacion = request.values['esterilizacion']
            propietario_id = request.values['propietario_id']

            mascota = Mascota.query.get(_idm)
            mascota.name=name 
            mascota.especie=especie
            mascota.raza=raza
            mascota.genero=genero
            mascota.color=color
            mascota.fechanac=fechanac
            mascota.esterilizacion=esterilizacion

            mascota.propietario_id=propietario_id

            db.session.commit()
            flash('Actualizado con exito')
            return redirect(url_for('mascota_router.index'))
mascotacontroller = MascotaController()