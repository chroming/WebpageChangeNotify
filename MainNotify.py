# -*- coding:utf-8 -*-

import requests
import time
from ReadJSON import *
from RequestsHeader import req_headers
from crawl_info import *


class WebVisit(object):
    def __init__(self):
        self.start_page_list = []  # 监控网址列表
        self.time_interval_num = 0  #
        self.attention_method = ''  # 监控内容匹配方式(正则,xpath,css)
        self.attention_exp = ''  # 监控内容匹配表达式
        self.return_method = ''  # 返回内容匹配表达式
        self.return_exp = ''  # 返回
        self.notify_email = ''  # 提醒邮箱
        self.notify_message = ''  # 提醒内容

    # 读取配置
    def get_config(self):
        json_dict = read_config()
        if json_dict:
            try:
                self.start_page_list =json_dict['StartPage']
                self.time_interval_num = json_dict['TimeInterval']
                self.attention_method = json_dict['Attention']['method']
                self.attention_exp = json_dict['Attention']['expression']
                self.return_method = json_dict['Return']['method']
                self.return_exp = json_dict['Return']['expression']
                self.notify_email = json_dict['Notify']['email']
                self.notify_message = json_dict['Notify']['message']
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
            time.sleep(30)
            return self.visit_web(url)

    # 根据配置获取要访问的url及要抓取的内容
    def visit_config(self):
        for url in self.start_page_list:
            page_text = self.visit_web(url)
            if page_text:
                if self.attention_method == 're':
                    result_list = re_find(page_text, self.attention_exp)
                elif self.attention_method == 'xpath':
                    result_list = xpath_find(page_text, self.attention_exp)
                elif self.attention_method == 'css':
                    result_list = css_find(page_text, self.attention_exp)
                else:
                    print u"Attention.method字段配置错误! 请检查后重试! "
                    exit()
                return result_list
            else:
                print u"get page error! "

    # 保存抓取结果
    def save_result(self):
        result_list = self.visit_config()
        for rl in result_list:
            pass
            # 此处使用数据库保存

    # 与上次的结果比对获得更新内容
    def compare_result(self):
        pass

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



















