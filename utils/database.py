# -*- coding: utf-8 -*-
import pymysql

from config.env import DB_CONFIG_PATH
from utils.load import load_ini


class MySqlBaseOPeration(object):
    """pymysql 原生SQL操作"""

    def __init__(self, env):
        self.conn = None
        self.env = env
        self.db_config = load_ini(DB_CONFIG_PATH)

    def connect(self):
        self.conn = pymysql.connect(host=self.db_config[self.env]["host"],
                                    port=self.db_config[self.env]["port"],
                                    user=self.db_config[self.env]["user"],
                                    password=self.db_config[self.env]["pwd"],
                                    database=self.db_config[self.env]["database"],
                                    charset="utf8")
    def close(self):
        self.conn.close()
