# -*- coding:utf-8 -*-

import requests
from ReadJSON import *
from RequestsHeader import req_headers


class WebVisit():
    def __init__(self):
        self.start_page_list = []
        self.time_interval_num = 0
        self.attention_method = ''
        self.attention_exp = ''
        self.return_method = ''
        self.return_exp = ''
        self.notify_email = ''
        self.notify_message = ''

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
            return self.visit_web(self, url)

    # 根据配置获取要访问的url及要抓取的内容
    def visit_config(self):
        for url in self.start_page_list:
            page_text = self.visit_web(url)
            if page_text:
                if self.attention_method == 're':
                    pass
                elif self.attention_method == 'xpath':
                    pass
                elif self.attention_method == 'css':
                    pass
                else:
                    print u"Attention.method字段配置错误! 请检查后重试! "
                    exit()












