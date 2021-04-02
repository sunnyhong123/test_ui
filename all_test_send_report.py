#!/usr/bin/python
# coding=utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header

import smtplib
import unittest
import time
import os


# =============发送邮件===================================
def sendReport(file_new):
    try:
        with open(file_new, 'rb') as f:
            mail_body = f.read()

        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header('自动化测试报告', 'utf-8')
        msg['From'] = 'hl13718441146@163.com'  # 发件地址
        msg['To'] = 'Sunny_hong@patazon.net';'Buck_xu@patazon.net';"zara_zeng@patazon.net"  # 收件人地址，多人以分号分隔

        smtp = smtplib.SMTP('smtp.163.com')
        smtp.set_debuglevel(1)
        smtp.login('hl13718441146@163.com', 'HODRMQVHELDZLLUL')  # 登录邮箱的账户和密码
        smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

        smtp.quit()
        print('test report has send out!')
    except Exception as e:
        return e


# ====================查找测试报告目录，找到最新生成的测试报告文件========
def newReport(testReport):
    try:
        lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件列表
        lists2 = sorted(lists)  # 获得按升序排序后的测试报告列表
        file_new = os.path.join(testReport, lists2[-1])  # 获取最后一个即最新的测试报告地址
        return file_new
    except Exception as e:
        return e


if __name__ == '__main__':
    #用例存放路径
    os_path = os.path.dirname(__file__)
    case_path = os.path.join(os_path, "test_case")

    # 报告存放路径
    os_report = os.path.dirname(__file__)
    report_path = os.path.join(os_report, "report")

    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')

    now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间
    filename = report_path + '\\' + now + 'result.html'  # 拼接出测试报告名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='MpowUI自动化测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()  # 这边曾错写成fp.close，导致发送邮件时正文怎么都发不出来

    new_report = newReport(report_path)  # 获取最新报告文件
    sendReport(new_report)  # 发送最新的测试报告

