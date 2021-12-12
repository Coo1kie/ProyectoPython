from sqlalchemy.orm import backref, relationship
from app import db
class Mascota(db.Model):
    __tablename__='mascota'
    idm=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(50))
    especie=db.Column(db.String(50), unique=True)
    raza=db.Column(db.String(50), unique=True)
    sexo=db.Column(db.String(20))
    color=db.Column(db.String(30))
    fechanac=db.Column(db.Date)
    esterilizacion=db.Column(db.String(2))
    foto=db.Column(db.String(30))

    #relacion foreign historial-mascota uno a muchos erro
    #hist_id=db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    #historial=relationship('HistorialC', back_populates="mascota")

    #relacion foreign historial-mascota uno a uno 1manera
    hc_id = db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    historial = relationship("Historial", back_populates="mascota")

    #relacion foreign historial-mascota uno a uno 2manera
    #hc_id = db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    #historial = relationship("Historial", backref=backref("mascota", uselist=False))

    #relacion foreign propietario-mascota
    propietario_id=db.Column(db.String(15), db.ForeignKey('propietario.ci'))
    propietario=relationship('Propietario', back_populates="mascota")

