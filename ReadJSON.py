# -*- coding:utf-8 -*-

import os
import json

conf_name = raw_input("Please input config name: ")
if not conf_name:
    name = 'config.json'


# 读取配置文件
def read_config():
    file_path = './%s' % conf_name
    if os.path.isfile(file_path):
        with open(file_path, 'r') as json_file:
            try:
                json_dict = json.load(json_file)
                return json_dict
            except:
                return None
    else:
        return None
