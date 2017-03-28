# -*- coding:utf-8 -*-

import os
import json
import sys

conf_name = sys.argv[1] if len(sys.argv) == 2 else 'config.json'
print sys.argv,len(sys.argv)


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
