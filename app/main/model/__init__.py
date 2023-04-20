# -*- coding: utf-8 -*-
from enum import Enum

from app.main import db


class DbCURD(Enum):
    ADD = 0
    UPDATE = 1
    DELETE = 2


class ModelBaseOperation(object):
    @staticmethod
    def db_commit(data, op: DbCURD):
        try:
            if op.value == DbCURD.ADD.value:
                db.session.add(data)
            elif op.value == DbCURD.DELETE.value:
                db.session.delete(data)
            elif op.value == DbCURD.UPDATE.value:
                pass
            db.session.commit()
            return True
        except Exception as e:
            return repr(e)

    @staticmethod
    def to_dict(obj):
        res = obj.__dict__
        if "_sa_instance_state" in res:
            res.pop("_sa_instance_state")
        return res
