from flask_restx import Api
from flask import Blueprint

from app.main.controller.status_controller import api as status_ns

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint,
    title="BACKEND PRINTCENTER",
    version="1.0",
    description="rotas para validação e requisição de dados",
)
api.add_namespace(status_ns, path="/status")
