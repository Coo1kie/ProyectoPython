__version__ = "0.1"
from flask import Flask
import secrets

UPLOAD_FOLDER = 'app/static/uploads/'
#app = Flask('app')

app = Flask(__name__, template_folder="views")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app.debug=True
from app.routes.main_router import main_router
app.register_blueprint(main_router)