from app import db
class Propietario(db.Model):
    __tablename__="propietario"
    ci=db.Column(db.String(15), primary_key=True)
    nombre=db.Column(db.String(50))
    apellido=db.Column(db.String(50))
    telcel=db.Column(db.String(50))

    #relacion uno a muchos
    #mascota=db.relationship('Mascota', backref="propietario")
    
