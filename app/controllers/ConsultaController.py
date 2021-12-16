from flask import render_template, url_for, request, redirect, flash
from app.models.Mascota import Mascota
from app.models.Consulta import Consulta
from app import db
class ConsultaController():
    def __init__(self):
        pass

    def index1(self):
        consultas=Consulta.query.join(Mascota).filter().all()
      
        return render_template('consultas/index.html', consultas=consultas) 
    def create(self):
        mascotas=Mascota.query.all()
        return render_template('consultas/create.html', mascotas=mascotas) #rederizar vista
    def store(self):
        if request.method == 'POST':
            motivo = request.form['motivo']
            fecha_c = request.form['fecha_c']
            peso = request.form['peso']
            anamnesis=request.form['anamnesis']
            tratamiento=request.form['tratamiento']
            mascota_id = request.values['mascota_id']
            
            consultaadd = Consulta(motivo=motivo, fecha_c=fecha_c, peso=peso,
            anamnesis=anamnesis,tratamiento=tratamiento, mascota_id=mascota_id)

            db.session.add(consultaadd)
            db.session.commit()
            flash('Consulta creado exitosamente')
            return redirect(url_for('consulta_router.index'))

    def delete(self, _idc):
        consulta = Consulta.query.get(_idc)
        db.session.delete(consulta)
        db.session.commit()
        flash('Eimnacion exitosa')
        return redirect(url_for('consulta_router.index'))
consultacontroller = ConsultaController()