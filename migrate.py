from app.models.User import User
from app.models.Propietario import Propietario
from app.models.HistorialC import HistorialC
from app.models.Mascota import Mascota
from app.models.Consulta import Consulta
from app.models.Vacuna import Vacuna
from app.models.Desparasitacion import Desparasitacion

from app import db

db.drop_all()
db.create_all()