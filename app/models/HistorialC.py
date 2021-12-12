from sqlalchemy.orm import backref, relationship
from app import db
class HistorialC(db.Model):
    __tablename__='historial'
    idhc=db.Column(db.Integer, primary_key=True, autoincrement=True)
    peso=db.Column(db.Float)

    #relaciones uno a muchos
    consulta=db.relationship('Consulta', backref="historial")
    vacuna=db.relationship('Vacuna', backref="historial")
    desparasitacion=db.relationship('Desparasitacion', backref="historial")

    #mascota=db.relationship('Mascota', backref="historial")
    mascota= relationship("Mascota", uselist=False, back_populates="historial")




