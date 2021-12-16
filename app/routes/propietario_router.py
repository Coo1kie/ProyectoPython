from flask import Blueprint
from flask_login.utils import login_required
from app.controllers.PropietarioController import propietariocontroller

propietario_router = Blueprint('propietario_router', __name__)

@propietario_router.route('/propietarios',methods=['GET'])
@login_required
def index():#ruta principal
    return propietariocontroller.index1() #index1 del controlador

@propietario_router.route('/propietarios/create',methods=['GET'])
@login_required
def create():#ruta 
    return propietariocontroller.create() # del controlador

@propietario_router.route('/propietarios/store',methods=['POST'])
@login_required
def store():#ruta 
    return propietariocontroller.store() # del controlador

@propietario_router.route('/propietarios/<int:ci>/delete',methods=['GET'])
@login_required
def delete(ci):#ruta 
    return propietariocontroller.delete(ci) # del controlador

@propietario_router.route('/propietarios/<int:ci>/edit',methods=['GET'])
@login_required
def edit(ci):#ruta 
    return propietariocontroller.edit(ci) # del controlador

@propietario_router.route('/propietarios/<int:ci>/update',methods=['POST'])
@login_required
def update(ci):#ruta 
    return propietariocontroller.update(ci) # del controlador