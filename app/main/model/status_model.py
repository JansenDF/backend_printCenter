from datetime import datetime
from .. import db


class Status(db.Model):
    """ Log Model for storing status related details """
    __tablename__ = "status"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(256), nullable=False)
    update_at = db.Column(db.DateTime, nullable=True)
    delete_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    delete_flag = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<Status '{}'>".format(self.description)
