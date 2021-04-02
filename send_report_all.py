#!/usr/bin/python
# coding=utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import random
import smtplib
import unittest
import time
import os
from public.reader_csv import read_save_txt

# =============发送邮件===================================
def sendReport(file_new):
    try:
        with open(file_new, 'rb') as f:
            mail_body = f.read()

        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header('自动化测试报告', 'utf-8')
        msg['From'] = 'hl13718441146@163.com'  # 发件地址
        msg['To'] = "Sunny_hong@patazon.net";"Buck_xu@patazon.net";"zara_zeng@patazon.net" # 收件人地址，多人以分号分隔

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

def get_rd_stord():
    """随机获取官网id"""
    store_id = [1, 2, 3, 5, 6, 8, 9, 10 ,11,12,13]
    rd_store_id = store_id[random.randrange(0, len(store_id))]
    # print(rd_store_id)
    read_save_txt("\data\store_id.txt",str(rd_store_id))
    if rd_store_id == 1:
        return "mpow"
    elif rd_store_id == 2:
        return "vt"
    elif rd_store_id == 3:
        return  "holife"
    elif rd_store_id == 5:
        return "ikich"
    elif rd_store_id == 6:
        return  "homasy"
    elif rd_store_id == 8:
        return  "litom"
    elif rd_store_id == 9:
        return  "iseneo"
    elif rd_store_id == 10:
        return  "iatmoko"
    elif rd_store_id == 11:
        return  "iokmee.com"
    elif rd_store_id == 12:
        return  "mpowjapan.co.jp"
    elif rd_store_id == 13:
        return  "ellesye.com"
    else:
        return "store id fail"

if __name__ == '__main__':
    store_txt = get_rd_stord()
    # os_path = os.getcwd().split("test_case")[0]
    # print(os_path)
    os_path = os.path.dirname(__file__)
    # print(os_path)

    case_path = os.path.join(os_path, "test_case")
    # print(case_path)

    # 报告存放路径
    # os_report = os.getcwd().split("report")[0]
    # print(os_report)
    os_report = os.path.dirname(__file__)
    # print(os_report)

    report_path = os.path.join(os_report, "report")
    # print(report_path)


    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py')

    now = time.strftime('%Y%m%d %H%M%S')  # 获取当前时间

    filename = report_path + '\\' + now + 'result.html'  # 拼接出测试报告名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='%s会员系统后台测试报告'%store_txt, description='用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report = newReport(report_path)  # 获取最新报告文件
    sendReport(new_report)  # 发送最新的测试报告

