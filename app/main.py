from flask import Flask
from .controllers.api import api_blueprints
from .controllers import app_blueprints

def create_app():
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static'
            )
    app.register_blueprint(api_blueprints())
    app.register_blueprint(app_blueprints())
    return app