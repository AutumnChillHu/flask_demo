# coding: utf-8
from enum import Enum

from sqlalchemy import Column, Integer, String

from app.main import db
from app.main.model import ModelBaseOperation


class TaskStatus(Enum):
    NEW = 0
    INPROCESS = 1
    DELETED = 2
    ALLSTATE = 99


class TaskInfo(db.Model):
    __tablename__ = 'task_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    state = Column(Integer, nullable=False, comment='0-新建；1-进行中；2-已结束；3-已删除')
