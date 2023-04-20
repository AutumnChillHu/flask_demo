# -*- coding: utf-8 -*-
from flask import Blueprint

index_bp = Blueprint("index", __name__)  # url_prefix默认为空
task_bp = Blueprint("task", __name__, url_prefix="/task")

from .main.controller import main, task
