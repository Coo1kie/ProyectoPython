from sqlalchemy.orm import relationship
from app import db
atiende_v = db.Table('atiende_v', db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('vacuna_id', db.Integer, db.ForeignKey('vacuna.idv'))
)
class Vacuna(db.Model):
    __tablename__='vacuna'
    idv=db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_v=db.Column(db.String(80))
    fecha_v=db.Column(db.Date)
    peso=db.Column(db.Float)
    prox_v=db.Column(db.Date)

    #relacion foreign
    hist_id=db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    historial=relationship('HistorialC', back_populates="vacuna")

    user = relationship(
        "User",
        secondary=atiende_v,
        back_populates="vacuna")
