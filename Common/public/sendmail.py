__author__ = 'Administrator'
#encoding: utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from Common.config import globalparam
from Common.public.projectPath import *
import logging
#from Common.public.readconfig import ReadConfig

# 配置收件人
recvaddress = ['zhangkai@zhinengdayi.com',
               'quanquan.lu@zhinengdayi.com',
               'shuqiong.tan@zhinengdayi.com']
# 邮箱用户名和密码
sendaddr_name = '179437774@qq.com'
sendaddr_pswd = 'lcccojdmaxkfbgfi'

class SendMail:
    def __init__(self,recver=None):
        """接收邮件的人：list or tuple"""
        if recver is None:
            self.sendTo = recvaddress   # 收件人这个参数，可以是list，或者tulp，以便发送给多人
        else:
            self.sendTo = recver

    def __get_report(self):
        """获取最新测试报告"""
        dirs = os.listdir(HtmlReport_path)
        dirs.sort()
        newreportname = dirs[len(dirs)-2]
        print('The new report name: {0}'.format(newreportname))
        return newreportname        # 返回的是测试报告的名字

    def __take_messages(self):
        newreport = self.__get_report()
        """生成邮件的内容，和html报告附件"""
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '自动化测试报告'      # 邮件的标题
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(HtmlReport_path,newreport), 'rb') as f:
            mailbody = f.read()             # 读取测试报告的内容
        html = MIMEText(mailbody,_subtype='html',_charset='utf-8')      # 将测试报告的内容放在 邮件的正文当中
        #html=MIMEText("测试报告",_charset='utf-8')
        self.msg.attach(html)       # 将html附加在msg里

        # html附件
        #att1 = MIMEText(HtmlReport_path+'\\'+newreport, 'base64', 'gb2312')
        att1 = MIMEText(mailbody, 'base64', 'gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        self.msg.attach(att1)

    def send(self):
        """发送邮件"""
        self.__take_messages()
        self.msg['from'] = sendaddr_name        # 发送邮件的人
        try:
            smtp = smtplib.SMTP_SSL('smtp.qq.com',465)  # 连接服务器
            smtp.login(sendaddr_name,sendaddr_pswd) # 登录的用户名和密码（注意密码是设置客户端授权码，因为使用用户密码不稳听，有时无法认证成功，导致登录不上，故无法发送邮件。）
            smtp.sendmail(self.msg['from'], self.sendTo, self.msg.as_string()) # 发送邮件
            smtp.close()
            logging.info("发送邮件成功")
        except Exception:
            logging.error('发送邮件失败')
            raise

if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()
