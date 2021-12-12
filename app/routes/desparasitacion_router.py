from flask import Blueprint
from app.controllers.DesparasitacionController import desparasitacioncontroller

desparasitacion_router = Blueprint('desparasitacion_router', __name__)

@desparasitacion_router.route('/desparasitaciones',methods=['GET'])
def index():#ruta principal
    return desparasitacioncontroller.index1() #index1 del controlador

@desparasitacion_router.route('/desparasitaciones/create',methods=['GET'])
def create():#ruta 
    return desparasitacioncontroller.create() # del controlador