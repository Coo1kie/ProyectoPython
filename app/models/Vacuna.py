from sqlalchemy.orm import relationship
from app import db

class Vacuna(db.Model):
    __tablename__='vacuna'
    idv=db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_v=db.Column(db.String(80))
    fecha_v=db.Column(db.Date)
    peso=db.Column(db.Float)
    prox_v=db.Column(db.Date)

    #relacion foreign
    #hist_id=db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    #historial=relationship('Historial', back_populates="vacuna")
    
    #relacion usuario-vacuna
    #user = relationship(
    #    "User",
    #    secondary=atiende_v,
    #    back_populates="vacuna")

        # Atributo o la clave foranea consulta-mascota
    mascota_id = db.Column(db.Integer, db.ForeignKey('mascota.idm'), nullable=False)
    #mascota=relationship('Mascota', back_populates="vacuna")
