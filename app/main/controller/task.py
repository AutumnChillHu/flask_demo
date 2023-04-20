# -*- coding: utf-8 -*-
from flask import redirect, url_for, request

from app import task_bp
from app.main.model.task_info import TaskStatus
from app.main.service.task import Task
from utils.request import get_request_args
from utils.response import response_format, HttpStatusCode


@task_bp.route("/taskinfo", methods=["POST"])
def query_one_task_info():
    args = get_request_args()
    if not args or len(args) > 1:
        return response_format(status_code=HttpStatusCode.ARGS_ERROR)
    key = list(args.keys())[0]
    return Task.query_task_info(key, args[key])


@task_bp.route("/allcount", methods=["GET"])
@task_bp.route("/allcount/state/<int:state>", methods=["GET"])
def count_task_by_state(state=TaskStatus.ALLSTATE.value):
    if state in TaskStatus._value2member_map_:
        return Task.count_task_by_state(state)
    return redirect(url_for("index.index", msg="redirect from {}".format(request.url)))


@task_bp.route("/create", methods=["POST"])
def create_task():
    args = get_request_args()
    if not args.get("name"):
        return response_format(status_code=HttpStatusCode.ARGS_ERROR)
    return Task.add_one_task(args)


@task_bp.route("/delete", methods=["POST"])
def delete_task():
    args = get_request_args()
    if not args.get("taskId"):
        return response_format(status_code=HttpStatusCode.ARGS_ERROR)
    return Task.delete_one_task(args)


@task_bp.route("/finish", methods=["POST"])
def finish_task():
    args = get_request_args()
    if not args.get("taskId"):
        return response_format(status_code=HttpStatusCode.ARGS_ERROR)
    return Task.finish_one_task(args)
