__author__ = 'Administrator'
#coding=utf-8
from Common.public.basepage import BasePage

class PublicityUserPage(BasePage):

    def return_username(self):
        return self.get_text('xpath->//div[@id="name"]//font')