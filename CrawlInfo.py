# -*- coding:utf-8 -*-

import re
from lxml.html import soupparser, tostring, HtmlElement


def re_find(text, exp):
    re_result_list = re.findall(r'%s' % exp, text, re.S)
    return re_result_list


def xpath_find(html, exp):
    root = soupparser.fromstring(html)
    result_ele = root.xpath(exp)
    return elements_to_unicodes(result_ele)


def elements_to_unicodes(eles):
    xpath_result = []
    for r in eles:
        xpath_result.append(tostring(r, encoding='utf-8').decode('utf-8') if isinstance(r, HtmlElement) else r)
    return xpath_result


def css_find(text, exp):
    pass
