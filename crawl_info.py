# -*- coding:utf-8 -*-

import re


# 正则表达式
def re_find(text, exp):
    re_result_list = re.findall(exp, text)
    return re_result_list


# xpath
def xpath_find(text, exp):
    pass


# css
def css_find(text, exp):
    pass
