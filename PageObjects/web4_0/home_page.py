#encoding: utf-8
from Common.public.basepage import BasePage


class HomePage(BasePage):

    def into_4_0_homepage(self, url="http://zhinengdayi.com/hbut"):
        self.open(url)

#顶部登录注册
    def move_to_qrc(self):
        """鼠标移动到扫码进入移动版"""
        self.move_to_element("id->mobile-qrcode")

    def qrc_visibility(self):
        """二维码可见"""
        return self.get_attribute("id->qrcode","style")

    def click_login(self):
        """click login btn"""
        self.click("xpath->//a[@class='fast-login']")

    def click_register(self):
        """click register btn"""
        self.click("xpath->//a[@class='fast_register']")

    def click_search_btn(self):
        """click searchbtn"""
        self.click("xpath->//p[@class='search-box']")

    def click_search_input(self):
        """click search input"""
        self.click("id->search")

    def type_search(self,text):
        self.type("id->search",text)

    def click_search(self):
        """点击搜索"""
        self.click("xpath->//div[@class='search-box']")

    def click_custom(self):
        """click zidingyixiang"""
        self.click("xpath->//li[@id='m01']/a")

#导航栏
    def click_logo(self):
        self.click("id->school-logo")

    def move_to_nav(self,num=2):
        """move to nav item"""
        self.move_to_element("xpath->//ul[@id='headerNav']/li[%s]" % num)

    def click_nav(self,num=2):
        """click and get nav item"""
        self.click("xpath->//ul[@id='headerNav']/li[%s]" % num)

    def get_navname(self,num=2):
        return self.get_text("xpath->//ul[@id='headerNav']/li[%s]/a" % num)

    def click_nav_artical(self,num1=2,num2=1):
        """click nav artical"""
        self.click("xpath->//ul[@id='headerNav']/li[%s]//li[%d]" % (num1, num2))

    def get_nav_articalname(self,num1=2,num2=1):
        return self.get_text("xpath->//ul[@id='headerNav']/li[%s]//li[%d]/a" % (num1, num2))

#招生快讯
    def click_alerts_more(self):
        self.click("xpath->//div[@id='admission-notice']//a[@class='toMore']")

    def click_alerts_headartical(self):
        """点击第一篇头部文章"""
        self.click("xpath->//div[@class='rt news-list']/h3/a")

    def get_alerts_headartical(self):
        """获取第一篇头部文章"""
        return self.get_text("xpath->//div[@class='rt news-list']/h3/a")

    def click_alerts_artical(self, num=1):
        self.click("xpath->//ul[@class='news-list']/li[%s]/a" % num)

    def get_alerts_artical(self, num=1):
        return self.get_text("xpath->//ul[@class='news-list']/li[%s]/a" % num)

#机器人
    def click_robot(self):
        self.click("id->jiqiren")

#招生信息
    def click_enrollment_artical(self,num=1):
        """点击招生信息文章"""
        self.click("xpath->//div[@id='enrollment-regulations']//li[%s]" % num)

    def get_enrollment_artical(self,num=1):
        return self.get_text("xpath->//div[@id='enrollment-regulations']//li[%s]//img" % num)

#快捷入口
    def click_quick_entry(self,num):
        """点击快捷入口"""
        self.click("xpath->//ul[@id='m05']/li[%s]" % num)

#招生章程
    def click_admissions_more(self):
        """点击招生章程更多"""
        self.click("xpath->//div[@id='admissions-guidelines']//a[@class='toMore']")

    def click_admissions_headartical(self,num=1):
        """点击招生章程头部文章"""
        self.click("xpath->//ul[@class='view']/li[%s]//p[@class='big-title with-img']/a" % num)
        return self.get_text("xpath->//ul[@class='view']/li[%s]//p[@class='big-title with-img']/a" % num)

    def click_admissions_articals(self,num=1):
        self.click("xpath->//ul[@class='bottom-list news-list']/li[%s]/a" % num)

