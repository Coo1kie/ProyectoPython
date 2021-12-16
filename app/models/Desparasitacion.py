from sqlalchemy.orm import relationship
from app import db

class Desparasitacion(db.Model):
    __tablename__='desparasitacion'
    idd=db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto=db.Column(db.String(80))
    fecha_d=db.Column(db.Date)
    peso=db.Column(db.Float)
    prox_d=db.Column(db.Date)

    #relacion foreign Historial-Desparasitacion
    #hist_id=db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    #historial=relationship('Historial', back_populates="desparasitacion")

    #relacion USUARIO-desparasitacion
    #user = relationship(
    #    "User",
    #    secondary=atiende_d,
    #    back_populates="desparacitacion")
    
    # Atributo o la clave foranea despaarasitacion-mascota
    #mascota_id = db.Column(db.Integer, db.ForeignKey('mascota.idm'), nullable=False)
    #mascota=relationship('Mascota', back_populates="desparasitacion")