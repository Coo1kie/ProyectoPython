from sqlalchemy.orm import backref, relationship
from app import db
class Historial(db.Model):
    __tablename__='historial'
    idhc=db.Column(db.Integer, primary_key=True, autoincrement=True)
    peso=db.Column(db.Float)
    fecha_p=db.Column(db.Date)

    #relaciones uno a muchos con Consulta, vacuna y desparasitacion
    consulta=db.relationship('Consulta', backref="historial")
    vacuna=db.relationship('Vacuna', backref="historial")
    desparasitacion=db.relationship('Desparasitacion', backref="historial")

    #mascota=db.relationship('Mascota', backref="historial")
    #mascota= relationship("Mascota", uselist=False, back_populates="historial")

    m_id = db.Column(db.Integer, db.ForeignKey('mascota.idm'))
    mascota = relationship("Mascota", back_populates="historial")




