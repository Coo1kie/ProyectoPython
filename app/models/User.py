from os import name
from app import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    cedula=db.Column(db.String(10))
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))
    username=db.Column(db.String(50))
    password=db.Column(db.String(50))