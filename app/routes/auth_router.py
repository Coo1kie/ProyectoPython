from flask import Blueprint
from app.controllers.AuthController import authcontroller

auth_router = Blueprint('auth_router', __name__)

@auth_router.route('/signup',methods=['GET','POST'])
def signup():#ruta principal
    return authcontroller.signup() #signup metodo  del controlador

@auth_router.route('/login',methods=['GET','POST'])
def login():#ruta principal
    return authcontroller.login() #signup metodo  del controlador  

@auth_router.route('/logout',methods=['GET','POST'])
def logout():#ruta principal
    return authcontroller.logout() #signup metodo  del controlador    