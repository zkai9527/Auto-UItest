#encoding: utf-8
__author__ = 'Administrator'
import unittest
import HTMLTestRunner
import time
from Common.public.projectPath import *
from Common.public import sendmail

def run():
    test_dir = TestCases_path+'\\web3_1'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
    """
    discover 方法里面有三个参数：
        case_dir：这个是待执行用例的目录。
        pattern：这个是匹配脚本名称的规则，test*.py 意思是匹配 test 开头的所有脚本。
        top_level_dir：这个是顶层目录的名称，一般默认等于 None 就行了。
    """
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = HtmlReport_path + '\\TestResult' + now + '.html'
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='3.1模板自动化测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)

    time.sleep(3)
    # 发送邮件
    mail = sendmail.SendMail()
    mail.send()

if __name__ == '__main__':
    run()