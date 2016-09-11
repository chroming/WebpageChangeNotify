# -*- coding:utf-8 -*-

import smtplib
import string

"""
弃用
"""

# 发送邮件函数
def SendMailTo(Subject, addr, result):
    BODY = string.join((
    'From:' '',
    'To:%s' % addr,
    'Subject:%s' % Subject,
    '%s' % result,
    ), '\r\n')

    server = smtplib.SMTP()
    server.connect('smtp.163.com', '25')
    server.login('', '')
    server.sendmail('sendmail', 'tomail', BODY)
    try:
        server.sendmail('sendmail', 'tomail', BODY)
        print "发送成功"
    except Exception as e:
        print "发送失败"
        server.quit()

if __name__ == '__main__':
    SendMailTo('test', '', 'test')