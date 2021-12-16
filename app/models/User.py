from flask_login import UserMixin
from enum import unique
from os import name

from sqlalchemy.orm import relationship
from app import db

class User(db.Model, UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    username=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(100))

  
    
    #relationshi
    #consulta = relationship(
    #  "Consulta",
    #   back_populates="users")
    
    #vacuna = relationship(
    #   "Vacuna",
    #   back_populates="users")
    
    #desparacitacion = relationship(
    #   "Desparacitacion",
    #    back_populates="users")