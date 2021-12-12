from flask import Blueprint
from app.controllers.MascotaController import mascotacontroller

mascota_router = Blueprint('mascota_router', __name__)

@mascota_router.route('/mascotas',methods=['GET'])
def index():#ruta principal
    return mascotacontroller.index1() #index1 del controlador

@mascota_router.route('/mascotas/create',methods=['GET'])
def create():#ruta 
    return mascotacontroller.create() # del controlador