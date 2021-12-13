__version__ = "0.1"
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import secrets

UPLOAD_FOLDER = 'app/static/uploads/'
#app = Flask('app')

app = Flask(__name__, template_folder="views")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#Conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/dbvet"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)
bycrypt=Bcrypt(app) #variable

secret=secrets.token_urlsafe(32)
app.config['SECRET_KEY']=secret

app.debug=True

from app.routes.auth_router import auth_router
app.register_blueprint(auth_router)

from app.routes.main_router import main_router
app.register_blueprint(main_router)

from app.routes.consulta_router import consulta_router
app.register_blueprint(consulta_router)

from app.routes.desparasitacion_router import desparasitacion_router
app.register_blueprint(desparasitacion_router)

from app.routes.historial_router import historial_router
app.register_blueprint(historial_router)

from app.routes.mascota_router import mascota_router
app.register_blueprint(mascota_router)


from app.routes.propietario_router import propietario_router
app.register_blueprint(propietario_router)

from app.routes.vacuna_router import vacuna_router
app.register_blueprint(vacuna_router)



