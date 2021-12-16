from sqlalchemy.orm import relationship
from app import db


class Consulta(db.Model):
    __tablename__='consulta'
    idc=db.Column(db.Integer, primary_key=True, autoincrement=True)
    motivo=db.Column(db.String(100))
    fecha_c=db.Column(db.Date)
    peso=db.Column(db.Float)
    anamnesis=db.Column(db.String(500))
    tratamiento=db.Column(db.String(500))

    #relacion foreign consulta-historial
    #hist_id=db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    #historial=relationship('Historial', back_populates="consulta")

    #relacion usuario-consulta
    #user = relationship(
    #    "User",
    #    secondary=atiende_c,
    #    back_populates="consulta")

    # Atributo o la clave foranea consulta-mascota
    #mascota_id = db.Column(db.Integer, db.ForeignKey('mascota.idm'), nullable=False)
    #mascota=relationship('Mascota', back_populates="consulta")

   



