__author__ = 'Administrator'
#encoding: utf-8
from Common.public.basepage import BasePage

class Robot_Page(BasePage):

    def have_Rengong(self):
        """判断是否显示分流弹框"""
        return self.element_exist("xpath->//div[@class='dialog-zixun']")
