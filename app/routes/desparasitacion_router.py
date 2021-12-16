from flask import Blueprint
from flask_login.utils import login_required
from app.controllers.DesparasitacionController import desparasitacioncontroller

desparasitacion_router = Blueprint('desparasitacion_router', __name__)

@desparasitacion_router.route('/desparasitaciones',methods=['GET'])
@login_required
def index():#ruta principal
    return desparasitacioncontroller.index1() #index1 del controlador

@desparasitacion_router.route('/desparasitaciones/create',methods=['GET'])
@login_required
def create():#ruta 
    return desparasitacioncontroller.create() # del controlador