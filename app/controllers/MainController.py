from app.models.User import User
from app import db
from flask import render_template
class MainController():
    def __init__(self):
        pass

    def index(self):
        users = User.query.all() #obtiene todo
        return render_template('home.html', users=users) #el primer users es el que manda al index
maincontroller = MainController()