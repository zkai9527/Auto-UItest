__author__ = 'Administrator'
#coding=utf-8

from Common.public.basepage import BasePage

class PublicityLoginPage(BasePage):

    def into_login_page(self):
        """打开登录页面"""
        self.open('http://report.zhinengdayi.com/spread/user/spreaderLoginPage')

    def type_username(self,name):
        """输入登录用户名"""
        self.type('id->inputUsername',name)

    def type_password(self,password):
        """输入登密码"""
        self.type('id->inputPassword',password)

    def click_usertype_student(self):
        """选择学生"""
        self.click('xpath->//div[@id="checkState"]/input[1]')

    def click_usertype_teacher(self):
        self.click_text('xpath->//div[@id="checkState"]/input[2]')

    def click_usertype_other(self):
        self.click_text('xpath->//div[@id="checkState"]/input[3]')

    def click_login_button(self):
        """点击登录按钮"""
        self.click('class->button ')

    def return_title(self):
        """返回该页面的title"""
        return self.get_title()