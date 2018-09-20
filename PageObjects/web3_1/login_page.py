__author__ = 'Administrator'
#encoding: utf-8
from Common.public.basepage import BasePage

class Login_page(BasePage):

#账号密码登录
    def click_typelogin(self):
        """点击账号密码登录"""
        self.click_text("账号密码登录")

    def get_titlename(self):
        """获取登录页面信息"""
        return self.get_text("xpath->//p[@class='login_title']")

    def can_to_see_login_content(self):
        """进入登录页可见登录框"""
        return self.element_exist("xpath->//p[@class='login_title']")

    def type_Account(self):
        """输入账号"""
        self.type("xpath->//input[@class='login_username_input']","179437774@qq.com")

    def type_password(self):
        """输入密码"""
        self.type("xpath->//input[@class='login_password_input']","123456")

    def click_login_btn(self):
        """点击登录按钮"""
        self.click("id->login_btn")
        self.wait(1)

    def click_register(self):
        """点击注册按钮"""
        self.click_text("免费注册")

    def click_return_psw(self):
        """点击找回密码"""
        self.click_text("忘记密码?")

#微信qq登录
    def click_quicklogin(self):
        """点击快捷登录"""
        self.click_text("快捷登录")

    def click_WX_login(self):
        """点击微信登录图标"""
        self.click("xpath->//div[@class='login_wechat']")

    def click_QQ_login(self):
        """点击QQ登录图标"""
        self.click("xpath->//div[@class='login_qq']")



