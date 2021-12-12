from flask import Blueprint
from app.controllers.PropietarioController import propietariocontroller

propietario_router = Blueprint('propietario_router', __name__)

@propietario_router.route('/propietarios',methods=['GET'])
def index():#ruta principal
    return propietariocontroller.index1() #index1 del controlador

@propietario_router.route('/propietarios/create',methods=['GET'])
def create():#ruta 
    return propietariocontroller.create() # del controlador

@propietario_router.route('/propietarios/store',methods=['POST'])
def store():#ruta 
    return propietariocontroller.store() # del controlador