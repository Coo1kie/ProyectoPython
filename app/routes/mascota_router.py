from flask import Blueprint
from flask_login.utils import login_required
from app.controllers.MascotaController import mascotacontroller

mascota_router = Blueprint('mascota_router', __name__)

@mascota_router.route('/mascotas',methods=['GET'])
@login_required
def index():#ruta principal
    return mascotacontroller.index1() #index1 del controlador

@mascota_router.route('/mascotas/create',methods=['GET'])
@login_required
def create():#ruta 
    return mascotacontroller.create() # del controlador
@mascota_router.route('/mascotas/store',methods=['POST'])
@login_required
def store():#ruta 
    return mascotacontroller.store() # del controlador

@mascota_router.route('/mascotas/<int:idm>/delete',methods=['GET'])
@login_required
def delete(idm):#ruta 
    return mascotacontroller.delete(idm) # del controlador

@mascota_router.route('/mascotas/<int:idm>/edit',methods=['GET'])
@login_required
def edit(idm):#ruta 
    return mascotacontroller.edit(idm) # del controlador

@mascota_router.route('/mascotas/update/<idm>',methods=['POST'])
@login_required
def update(idm):#ruta 
    return mascotacontroller.update(idm) # del controlador
