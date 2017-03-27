# -*- coding:utf-8 -*-

import requests
import time
from RequestsHeader import req_headers
from CrawlInfo import *
from read_DB import *
from SendMail import *
from FilterResult import *
import random

METHOD_DICT = {
    're': re_find,
    'xpath': xpath_find,
    'css': css_find
}


class WebVisit(object):
    def __init__(self):
        self.start_page_list = []  # 监控网址列表
        self.time_interval_num = 0  # 时间间隔
        self.fail_time_interval_num = 0  # 访问失败再次访问时间间隔
        self.attention_method = ''  # 监控内容匹配方式(正则,xpath,css)
        self.attention_exp = ''  # 监控内容匹配表达式
        self.return_method = ''  # 返回内容匹配表达式
        self.return_exp = ''  # 返回
        self.notify_email = ''  # 提醒邮箱
        self.notify_message = ''  # 提醒内容
        self.filter_exp = ''  # 结果过滤正则表达式
        self.filter_num = 0  # 结果过滤group

    # 读取配置
    def get_config(self):
        json_dict = read_config()
        if json_dict:
            try:
                self.start_page_list = json_dict['StartPage']
                self.time_interval_num = json_dict['TimeInterval']
                self.fail_time_interval_num = json_dict['FailTimeInterval']
                self.attention_method = json_dict['Attention']['method']
                self.attention_exp = json_dict['Attention']['expression']
                self.return_method = json_dict['Return']['method']
                self.return_exp = json_dict['Return']['expression']
                self.notify_email = json_dict['Notify']['email']
                self.notify_message = json_dict['Notify']['message']
                self.filter_exp = json_dict['Filter']['expression']
                self.filter_num = json_dict['Filter']['num']
            except:
                print u"配置不完整! 请修改后重试! "
                exit()
        else:
            print u"配置文件不存在或内容有误! 请检查后重试! "
            exit()

    # 访问url
    def visit_web(self, url):

        try:
            page = requests.get(url, headers=req_headers, allow_redirects=True)
            return page.text
        except:
            print u"网络访问失败! "
            time.sleep(self.fail_time_interval_num + random.randint(10, 30))
            return self.visit_web(url)

    # 根据配置获取要访问的url及要抓取的内容
    def visit_config(self):
        result_list_all = []
        for url in self.start_page_list:
            result_list = []
            page_text = self.visit_web(url)
            if page_text:
                print u"%s访问成功！ " % url
                if self.attention_method in METHOD_DICT:
                    result_list = METHOD_DICT[self.attention_method](page_text, self.attention_exp)
                else:
                    print u"Attention.method字段配置错误! 请检查后重试! "
                    exit()
                print u"抓取成功！  "
                result_list_all.extend(result_list)
            else:
                print u"get page %s error! " % url
            time.sleep(self.fail_time_interval_num + random.randint(10, 30))
            yield result_list
        # return result_list_all

    # 保存抓取结果
    def save_result(self):
        try:
            create_table('%s' % conf_name, 'result')
        except:
            pass
        while 1:
            result_list = self.visit_config()
            for rl in result_list:
                rl = filter_result(rl, self.filter_exp, self.filter_num)
                new_list = write_db('%s' % conf_name, 'result', rl)
                if new_list:
                    new_json = json.dumps(new_list, encoding="UTF-8", ensure_ascii=False)
                    SendMailTo("有更新啦！ ", new_json)
                # time.sleep(self.time_interval_num + random.randint(1, 100))


if __name__ == '__main__':
    newVisit = WebVisit()
    newVisit.get_config()
    newVisit.save_result()


















