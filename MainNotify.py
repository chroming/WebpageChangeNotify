# -*- coding:utf-8 -*-

import requests
import time
from RequestsHeader import req_headers
from crawl_info import *
from read_DB import *
from sendMail import *
from FilterResult import *
import random


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
                if self.attention_method == 're':
                    result_list = re_find(page_text, self.attention_exp)
                elif self.attention_method == 'xpath':
                    result_list = xpath_find(page_text, self.attention_exp)
                elif self.attention_method == 'css':
                    result_list = css_find(page_text, self.attention_exp)
                else:
                    print u"Attention.method字段配置错误! 请检查后重试! "
                    exit()
                print u"抓取成功！  "
                result_list_all.extend(result_list)
            else:
                print u"get page %s error! " % url
            time.sleep(self.fail_time_interval_num + random.randint(10, 30))
        return result_list_all

    # 保存抓取结果
    def save_result(self):
        try:
            create_table('%s' % conf_name, 'result')
        except:
            pass
        while 1:
            result_list = self.visit_config()
            result_list = filter_result(result_list, self.filter_exp, self.filter_num)
            new_list = write_db('%s' % conf_name, 'result', result_list)
            print new_list
            #new_list = filter_result(new_list, self.filter_exp, self.filter_num)
            if new_list:
                new_json = json.dumps(new_list, encoding="UTF-8", ensure_ascii=False)
                SendMailTo("有更新啦！ ", new_json)
            time.sleep(self.time_interval_num)


    '''
    # 根据配置获取返回结果需要抓取的内容
    def return_config(self):
        for url in self.start_page_list:
            page_text = self.visit_web(url)
            if page_text:
                if self.return_method == 're':
                    result_list = re_find(page_text, self.return_exp)
                elif self.return_method == 'xpath':
                    result_list = xpath_find(page_text, self.return_exp)
                elif self.return_method == 'css':
                    result_list = css_find(page_text, self.return_exp)
                else:
                    print u"Return.method字段配置错误! 请检查后重试! "
                    exit()
                return result_list
            else:
                print u"get page error! "

    #
    def save_return(self):
        return_list = self.return_config()
        for rl in return_list:
            pass
    '''

if __name__ == '__main__':
    newVisit = WebVisit()
    newVisit.get_config()
    newVisit.save_result()


















