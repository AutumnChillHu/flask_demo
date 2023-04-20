# -*- coding: utf-8 -*-
"""Flask.request 请求对象"""
from flask import request


def request_attrs():
    """Flask.request 请求对象的常用属性"""

    print(request.headers, type(request.headers))  # 获取Headers，得到EnvironHeaders格式数据，同dict访问，推荐转成dict。
    print(request.cookies, type(request.cookies))  # 获取，得到ImmutableMultiDict格式数据，推荐转成dict。

    if request.method == "GET":
        # 获取GET参数，得到ImmutableMultiDict格式数据。
        print(request.args, type(request.args))
        # 适用于GET&POST请求，对于GET请求等同于request.args，得到CombinedMultiDict格式数据。
        print(request.values, type(request.values))
    elif request.method == "POST":
        # 获取POST参数，适用于Content-Type=application/json。得到dict格式数据。等同于request.get_json()
        print(request.json, type(request.json))

        # 获取POST参数，适用于Content-Type=multipart/form-data或application/x-www-form-urlencoded，常见于postman里。
        # 得到ImmutableMultiDict格式数据。
        print(request.form, type(request.form))
        # 适用于GET&POST请求，对于POST请求等同于request.form，得到CombinedMultiDict格式数据。
        print(request.values, type(request.values))

        # 获取POST参数，适用于Content-Type=text/plain。得到bytes格式数据。等同于request.get_data()
        print(request.data, type(request.data))

    # 获取上传文件
    print(request.files, type(request.files))


def get_request_params():
    if request.method == 'GET':
        # MultiDict/ImmutableMultiDict格式，如果key不存在，会返回HTTP 400
        # 推荐转化成Dict，如果key不存在，会报KeyError
        data = request.args.to_dict()
    else:
        data = request.json if request.headers.get("Content-Type") == "application/json" else request.form.to_dict()
    return data