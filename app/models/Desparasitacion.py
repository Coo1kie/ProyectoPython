from sqlalchemy.orm import relationship
from app import db
atiende_d = db.Table('atiende_d', db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('desparasitacion_id', db.Integer, db.ForeignKey('desparasitacion.idd'))
)
class Desparasitacion(db.Model):
    __tablename__='desparasitacion'
    idd=db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto=db.Column(db.String(80))
    fecha_d=db.Column(db.Date)
    peso=db.Column(db.Float)
    prox_d=db.Column(db.Date)

    #relacion foreign
    hist_id=db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    historial=relationship('HistorialC', back_populates="desparasitacion")

    user = relationship(
        "User",
        secondary=atiende_d,
        back_populates="desparacitacion")