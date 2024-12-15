from flask import Blueprint
from .index_api import index_bp as index_api_bp

def api_blueprints():
    api_bp = Blueprint('api', __name__, url_prefix='/api')

    api_bp.register_blueprint(index_api_bp)

    return api_bp