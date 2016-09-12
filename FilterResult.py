# -*- coding:utf-8 -*-
import re


def filter_result(result_list, exp, num):
    result = []
    for rl in result_list:
        re_result = re.search(exp, rl)
        try:
            result.append(re_result.group(num))
        except:
            pass
    return result
