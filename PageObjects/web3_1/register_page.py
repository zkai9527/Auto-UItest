__author__ = 'Administrator'
#encoding: utf-8
from Common.public.basepage import BasePage

class Register_Page(BasePage):

    def have_register_title(self):
        """获取注册页面标题"""
        return self.element_exist("xpath->//p[@class='register_titles']")