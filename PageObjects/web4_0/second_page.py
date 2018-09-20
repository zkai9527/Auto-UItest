#encoding: utf-8
from Common.public.basepage import BasePage


class SecondPage(BasePage):

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
        self.click("xpath->//div[@class='input-group']//i[@class='comicon-search']")

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

#左侧菜单栏
    def get_leftMenu(self):
        """获取左侧菜单栏一级菜单名"""
        self.wait(1)
        return self.get_text("xpath->//div[@class='themeMenuHead']")

    def get_leftSecondMenu(self, num):
        """获取左侧菜单栏二级菜单名"""
        self.wait(1)
        return self.get_text("xpath->//ul[@class='article-list']/li[%s]" % num)

    def get_leftThirdMenu(self, num1, num2):
        """获取左侧菜单栏第三级菜单名"""
        return self.get_text("xpath->//ul[@class='article-list']/li[%s]//a[@class='lastCat'][%s]/span" % (num1, num2))

    def click_leftSecondMenu(self, num):
        """点击左侧菜单栏二级菜单名"""
        self.click("xpath->//ul[@class='article-list']/li[%s]" % num)

    def click_leftThirdMenu(self, num1, num2):
        """点击左侧菜单栏第三级菜单名"""
        self.click("xpath->//ul[@class='article-list']/li[%s]//a[@class='lastCat'][%s]" % (num1, num2))

    # def get_third_style(self,num):
    #     """获取三级菜单是否可见"""
    #     return self.get_attribute("xpath->//ul[@class='article-list']/li[%s]/div" % num, "style")

#右侧菜单栏
    def click_robot(self):
        self.click("xpath->//a[@id='robot']/img")

    def click_Announcement(self):
        """点击右侧招录公告"""
        self.click("id->book1")
        #return self.get_text("id->book1")

    def click_vedio(self):
        self.click("id->book2")
        #return self.get_text("id->book2")

    def click_photo(self):
        self.click("id->book3")
        #return self.get_text("id->book3")

#中间文章部分
    def get_list_footprint(self):
        """获取列表面包屑内容"""
        return self.get_text("id->footprint")

    def get_artical_footprint(self):
        """获取详情页面包屑内容"""
        return self.get_text("id->footprint01")

    def click_listingArtical(self,num=1):
        """点击列表页文章标题"""
        self.click("xpath->//ul[@id='articleList']/a[%s]" % num)

    def can_see_list(self):
        return self.element_exist("id->articleList")

    def get_listingArtical(self,num=1):
        return self.get_text("xpath->//ul[@id='articleList']/a[%s]/span[@class='title']" % num)

    def get_ArticalTitle(self):
        return self.get_text("id->article-title")

    def click_next(self):
        """点击下一篇"""
        self.click("xpath->//a[@class='next-article']")

    def click_prev(self):
        """点击上一篇"""
        self.click("xpath->//a[@class='prev-article']")

    def click_backlist(self):
        """点击回到列表"""
        self.click("xpath->//a[@class='back-to-list']")

    def get_next_style(self):
        """点击下一篇"""
        return self.get_attribute("xpath->//a[@class='next-article']", "style")

    def get_prev_style(self):
        """点击上一篇"""
        self.get_attribute("xpath->//a[@class='prev-article']", "style")

    def get_backlist_style(self):
        """点击回到列表"""
        self.get_attribute("xpath->//a[@class='back-to-list']", "style")

#专业简介页面
    def get_majorname(self,num):
        return self.get_text("xpath->//tbody/tr[%s]/td[3]/a" % num)

    def click_major(self,num):
        self.click("xpath->//tbody/tr[%s]/td[3]/a" % num)

    def click_department(self,departmentname):
        self.click_text(departmentname)

#专业详情页
    def click_enrollment_plan(self):
        self.click("id->enrollmentPlan")

    def click_history_enrollment(self):
        self.click("id->historyEnrollment")

#院系详情页
    def click_department_url(self):
        self.click("id->officialWebsite")

    def click_majorname(self,num):
        self.click("xpath->//tbody[@id='tbody1']/tr[%s]/td[1]/a" % num)

#招生计划
    def click_enrollment_major(self):
        self.click("id->major-tab")

    def click_enrollment_school(self):
        self.click("xpath->//li[@id='major-tab']//following-sibling::li")

    def get_enrollment_major(self):
        return self.get_attribute("id->major-con", "style")

    def get_enrollment_school(self):
        return self.get_attribute("xpath->//div[@class='tab-con'][2]", "style")

    def can_see_plan_table(self):
        return self.element_exist("id->enrollPlanDetail")

#录取数据
    def click_admission_major(self):
        self.click("id->major-tab")

    def get_admission_major(self):
        return self.get_attribute("id->major-con", "style")

    def get_admission_school(self):
        return self.get_attribute("xpath->//div[@class='tab-con']", "style")

#搜索后的页面
    def get_search_list(self):
        return self.get_text("xpath->//div[@id='searchInfo']//font")
