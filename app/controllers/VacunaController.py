from flask import render_template, url_for, request, redirect, flash
from app.models.Mascota import Mascota
from app.models.Vacuna import Vacuna
from app import db
class VacunaController():
    def __init__(self):
        pass

    def index1(self):
        vacunas=Vacuna.query.join(Mascota).filter().all()
        return render_template('vacunas/index.html', vacunas=vacunas) 


    def create(self):
        mascotas=Mascota.query.all()
        return render_template('vacunas/create.html', mascotas=mascotas) #rederizar vista
    
    def store(self):
        if request.method == 'POST':
            tipo_v = request.form['tipo_v']
            fecha_v = request.form['fecha_v']
            prox_v=request.form['prox_v']
            mascota_id = request.values['mascota_id']
            
            vacunaadd = Vacuna(tipo_v=tipo_v, fecha_v=fecha_v, prox_v=prox_v, mascota_id=mascota_id)

            db.session.add(vacunaadd)
            db.session.commit()
            flash('Vacuna creado exitosamente')
            return redirect(url_for('vacuna_router.index'))

    def delete(self, _idv):
        vacuna = Vacuna.query.get(_idv)
        db.session.delete(vacuna)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('vacuna_router.index'))
vacunacontroller = VacunaController()