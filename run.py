#coding=utf-8

import unittest
import time
from config import globalparam
from public.common import sendmail
from public.common import HTMLTestRunner

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('-%Y-%m-%d_%H-%M-%S')
    reportname = globalparam.report_path + '/' + 'TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='XXX平台自动化测试报告',
            description='Testcases Detail'
        )
        runner.run(suite)
    time.sleep(3)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

if __name__=='__main__':
    run()