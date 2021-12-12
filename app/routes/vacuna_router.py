from flask import Blueprint
from app.controllers.VacunaController import vacunacontroller

vacuna_router = Blueprint('vacuna_router', __name__)

@vacuna_router.route('/vacunas',methods=['GET'])
def index():#ruta principal
    return vacunacontroller.index1() #index1 del controlador

@vacuna_router.route('/vacunas/create',methods=['GET'])
def create():#ruta 
    return vacunacontroller.create() # del controlador