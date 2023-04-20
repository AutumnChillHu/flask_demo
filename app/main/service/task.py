# -*- coding: utf-8 -*-
import time

from sqlalchemy.exc import NoResultFound

from app.main.model import DbCURD, ModelBaseOperation
from app.main.model.task_info import TaskInfo, TaskStatus
from utils.response import HttpStatusCode, response_format


class Task(object):

    @staticmethod
    def query_task_info(key, value):
        if key == "id":
            task = TaskInfo.query.filter_by(id=int(value)).first()
            time.sleep(2)
        elif key == "name":
            task = TaskInfo.query.filter_by(name=value).first()
        elif key == "state":
            task = TaskInfo.query.filter_by(state=int(value)).first()
        else:
            return response_format(status_code=HttpStatusCode.ARGS_ERROR, data="wrong key")
        if not task:
            return response_format(status_code=HttpStatusCode.OK, data="数据不存在 key={} value{}".format(key, value))
        return response_format(status_code=HttpStatusCode.OK, data=ModelBaseOperation.to_dict(task))

    @staticmethod
    def count_task_by_state(state):
        if state == TaskStatus.ALLSTATE.value:
            return response_format(status_code=HttpStatusCode.OK, data=TaskInfo.query.count())
        return response_format(status_code=HttpStatusCode.OK, data=TaskInfo.query.filter_by(state=state).count())

    @staticmethod
    def add_one_task(args):
        new_task = TaskInfo(name=args["name"], state=0)
        res = ModelBaseOperation.db_commit(new_task, DbCURD.ADD)
        if res == True:
            return response_format(status_code=HttpStatusCode.OK, data=new_task.id)
        return response_format(status_code=HttpStatusCode.ERROR, data=res)

    @staticmethod
    def delete_one_task(args):
        task = TaskInfo.query.get(args["taskId"])
        if not task:
            return response_format(status_code=HttpStatusCode.ERROR,
                                   data="删除失败，任务task_id={}不存在".format(args["taskId"]))

        res = ModelBaseOperation.db_commit(task, DbCURD.DELETE)
        if res == True:
            return response_format(status_code=HttpStatusCode.OK, data=res)
        return response_format(status_code=HttpStatusCode.ERROR, data=res)

    @staticmethod
    def finish_one_task(args):
        task = TaskInfo.query.get(args["taskId"])
        if not task:
            return response_format(status_code=HttpStatusCode.ERROR,
                                   data="更新失败，任务task_id={}不存在".format(args["taskId"]))
        task.state = 2
        res = ModelBaseOperation.db_commit(task, DbCURD.UPDATE)
        if res == True:
            return response_format(status_code=HttpStatusCode.OK, data=res)
        return response_format(status_code=HttpStatusCode.ERROR, data=res)
