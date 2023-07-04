from flask import request
from flask_restx import Resource

from app.main.utils.dto import StatusDTO
from app.main.service.status_service import (
    create_status,
    get_a_status,
    get_all_status,
    update_a_status,
    delete_a_status,
)


api = StatusDTO.api
_status = StatusDTO.status


@api.route("/")
class StatusList(Resource):
    @api.doc("list_of_registered_status")
    @api.marshal_list_with(_status, envelope="data")
    def get(self):
        """List all registered status"""
        return get_all_status()

    @api.response(200, "Status successfully created.")
    @api.doc("create a new status")
    @api.expect(_status, validate=True)
    def post(self):
        """Creates a new Status"""
        data = request.json
        return create_status(data=data)


@api.route("/<int:id>")
@api.param("id", "The Status identifier")
@api.response(404, "Status not found.")
class StatusRecord(Resource):
    @api.doc("get a status")
    @api.marshal_with(_status)
    def get(self, id):
        """get a status given its identifier"""
        return get_a_status(id=id)

    @api.doc("delete a status")
    @api.response(204, "Status successfully deleted")
    def delete(self, id):
        """Delete a status given its identifier"""
        status = get_a_status(id)
        if status.delete_flag:
            api.abort(404)
        else:
            return delete_a_status(id=id)

    @api.doc("update a status")
    @api.response(200, "Status successfully updated")
    @api.expect(_status, validate=True)
    def put(self, id):
        """Update a status given its identifier"""
        status = get_a_status(id)
        data = request.json
        if status.delete_flag:
            api.abort(404)
        else:
            return update_a_status(id=id, data=data)
