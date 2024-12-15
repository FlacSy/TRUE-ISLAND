from flask import Blueprint
from .index import index_bp


def app_blueprints():
    app_bp = Blueprint('app', __name__)

    app_bp.register_blueprint(index_bp)

    return app_bp