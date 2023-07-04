from datetime import datetime

from flask import jsonify
from flask import request

from app.main import db
from app.main.model.status_model import Status


def create_status(data):
    status = Status.query.filter_by(description=data["description"]).all()
    if not status:
        try:
            data = request.get_json()
            _description = data.get("description")
            new_status = Status(description=_description)
            db.session.add(new_status)
            db.session.commit()
            print(new_status)
            return jsonify("Status successfully created")
        except Exception as e:
            print(e)
            return jsonify("Connection to database failed.")
    else:
        return jsonify("Status already exists.")


def get_all_status():
    status = Status.query.all()
    return status


def get_a_status(id):
    status = Status.query.filter_by(id=id).all()
    return status


def update_a_status(id, data):
    try:
        status_update = Status.query.filter_by(id=id).first()
        status_update.description = (
            data.get("description") if data.get("description") is not None else ""
        )
        status_update.update_at = datetime.utcnow()
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Status successfully updated.",
        }

        return response_object, 201
    except Exception as e:
        print(e)
        response_object = {"status": "failed", "message": e}
        return response_object, 400


def delete_a_status(id):
    try:
        status_delete = Status.query.filter_by(id=id).first()
        status_delete.delete_at = datetime.utcnow()
        status_delete.delete_flag = True
        db.session.commit()
        response_object = {
            "status": "success",
            "message": "Status successfully deleted.",
        }
        return response_object, 201
    except Exception as e:
        print(e)
        response_object = {"status": "failed", "message": e}
        return response_object, 400
