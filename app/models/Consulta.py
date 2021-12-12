from sqlalchemy.orm import relationship
from app import db
atiende_c = db.Table('atiende_c', db.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('consulta_id', db.Integer, db.ForeignKey('consulta.idc'))
)


class Consulta(db.Model):
    __tablename__='consulta'
    idc=db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha_c=db.Column(db.Date)
    peso=db.Column(db.Float)
    anamnesis=db.Column(db.String(500))
    diagnostico=db.Column(db.String(500))
    tratamiento=db.Column(db.String(500))

    #relacion foreign consulta-historial
    hist_id=db.Column(db.Integer, db.ForeignKey('historial.idhc'))
    historial=relationship('HistorialC', back_populates="consulta")


    user = relationship(
        "User",
        secondary=atiende_c,
        back_populates="consulta")



