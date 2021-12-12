from flask import Blueprint
from app.controllers.ConsultaController import consultacontroller

consulta_router = Blueprint('consulta_router', __name__)

@consulta_router.route('/consultas',methods=['GET'])
def index():#ruta principal
    return consultacontroller.index1() #index1 del controlador
@consulta_router.route('/consultas/create',methods=['GET'])
def create():#ruta 
    return consultacontroller.create() # del controlador