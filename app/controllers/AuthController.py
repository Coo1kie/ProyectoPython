import flask_sqlalchemy
from app.models.User import User
from app import db, bycrypt, app
from flask_login import LoginManager, login_manager, login_user, logout_user, current_user
from flask import render_template, request, flash, redirect, url_for, session
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view= 'auth_router.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class AuthController():
    def __init__(self):
        pass

    def signup(self):
        if request.method=='POST':
            name = request.form['name']
            email = request.form['email']# req llega de la vista
            username = request.form['username']
            password = bycrypt.generate_password_hash(request.form['password'])

            user=User(name=name, email=email, username=username, password=password)

            db.session.add(user)
            db.session.commit()

            flash('Usuario Registrado!')
            return render_template('auth/login.html')
        return render_template('auth/signup.html') #renderiza la vista signup

    def login(self):
        if request.method=='POST':
            user=User.query.filter_by(username=request.form['username']).first()
            if user:
                if bycrypt.check_password_hash(user.password, request.form['password']):
                    login_user(user)
                    return redirect(url_for('main_router.main'))

            flash('Usuario no existe, o credenciales no Vaidas')
            return redirect(url_for('auth_router.login'))
        return render_template('auth/login.html') #renderiza la vista 
        
    def logout(self):
        session.clear()
        logout_user()
        return redirect(url_for('auth_router.login'))
authcontroller = AuthController()