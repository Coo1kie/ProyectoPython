from flask import Blueprint
from flask_login.utils import login_required
from app.controllers.VacunaController import vacunacontroller

vacuna_router = Blueprint('vacuna_router', __name__)

@vacuna_router.route('/vacunas',methods=['GET'])
@login_required
def index():#ruta principal
    return vacunacontroller.index1() #index1 del controlador

@vacuna_router.route('/vacunas/create',methods=['GET'])
@login_required
def create():#ruta 
    return vacunacontroller.create() # del controlador

@vacuna_router.route('/vacunas/store',methods=['POST'])
@login_required
def store():#ruta 
    return vacunacontroller.store() # del controlador

@vacuna_router.route('/vacunas/<int:idv>/delete',methods=['GET'])
@login_required
def delete(idv):#ruta 
    return vacunacontroller.delete(idv) # del controlador