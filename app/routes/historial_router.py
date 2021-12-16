from flask import Blueprint
from flask_login.utils import login_required
from app.controllers.HistorialController import historialcontroller

historial_router = Blueprint('historial_router', __name__)

@historial_router.route('/historiales',methods=['GET'])
@login_required
def index():#ruta principal
    return historialcontroller.index1() #index1 del controlador

@historial_router.route('/historial/create',methods=['GET'])
@login_required
def create():#ruta 
    return historialcontroller.create() # del controlador