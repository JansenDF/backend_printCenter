from flask_restx import Namespace, fields


class StatusDTO:
    api = Namespace("status", description="status related operations")
    status = api.model(
        "status", {"description": fields.String(required=True, description="status")}
    )
