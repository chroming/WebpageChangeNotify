# -*- coding:utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from ReadJSON import *


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(),addr.encode('utf-8') if isinstance(addr, unicode) else addr))


mail_dict = read_config()
from_addr = mail_dict['Mail']['from_addr']
password = mail_dict['Mail']['password']
to_addr= mail_dict['Mail']['to_addr']
smtp_server = mail_dict['Mail']['smtp_server']


def SendMailTo(subject, result):
    msg = MIMEText('%s' % result, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'监控爬虫 <%s>' % from_addr)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

if __name__ == '__main__':
    SendMailTo('test', 'test')
