# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config_by_name[config_name])
    # db.init_app(app)
    # flask_bcrypt.init_app(app)

    return app
