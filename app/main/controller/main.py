# -*- coding: utf-8 -*-
from app import index_bp
from utils.request import get_request_args
from utils.response import response_format, HttpStatusCode


@index_bp.route("/", methods=["GET"])
def index():
    args = get_request_args()
    return response_format(status_code=HttpStatusCode.OK, data="hello world ! {}".format(args))
