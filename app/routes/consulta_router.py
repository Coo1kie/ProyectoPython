from flask import Blueprint
from flask_login.utils import login_required
from app.controllers.ConsultaController import consultacontroller

consulta_router = Blueprint('consulta_router', __name__)

@consulta_router.route('/consultas',methods=['GET'])
@login_required
def index():#ruta principal
    return consultacontroller.index1() #index1 del controlador
@consulta_router.route('/consultas/create',methods=['GET'])
@login_required
def create():#ruta 
    return consultacontroller.create() # del controlador