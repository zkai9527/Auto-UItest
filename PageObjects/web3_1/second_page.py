__author__ = 'Administrator'
#encoding: utf-8
from Common.public.basepage import BasePage
import sys


class Second_Page(BasePage):

#head
    def click_logo(self):
        """点击logo"""
        self.click("xpath->//div[@class='header_left']")

#导航栏
    def move_to_secondPage_Nav(self,num=1):
        """移动到导航栏菜单"""
        self.move_to_element("xpath->//ul[@class='first_nav_new']/li[%s]" % num)

    def click_Nav_secondPage_Menu(self,num=1):
        """点击菜单"""
        self.click("xpath->//ul[@class='first_nav_new']/li[%s]" % num)

    def get_Nav_secondPage_Menu(self,num=1):
        """获取导航栏菜单名"""
        return self.get_text("xpath->//ul[@class='first_nav_new']/li[%s]//a[@class='first_msg']" % num)

    def get_Nav_secondPage_secondMenu(self):
        """获取该菜单下二级菜单名"""
        return self.get_text("xpath->//ul[@class='first_nav_new']/li[1]//ul/li[1]")

    def click_Nav_secondPage_secondMenu(self):
        """点击二级菜单名"""
        self.click("xpath->//ul[@class='first_nav_new']/li[1]//ul/li[1]")
#面包屑
    def get_first_catmenu(self):
        """获取面包屑一级菜单名"""
        return self.get_text("xpath->//a[@class='aur']")

    def get_second_catmenu(self):
        """获取面包屑二级菜单名"""
        return self.get_text("xpath->//a[@class='cur']")

    def get_third_catmenu(self):
        """获取面包屑三级菜单名"""
        return self.get_text("xpath->//a[@class='sur']")

#文章内容详情页
    def get_article_title(self):
        """获取文章详情页标题"""
        return self.get_text("xpath->//h1[@class='tips01']")

    def click_Enrollment_plan(self):
        """点击专业详情页招生计划"""
        self.click("xpath->//a[@class='look_detail']")

    def click_History_admission(self):
        """点击专业详情页历史录取"""
        self.click("xpath->//a[@class='look_history']")

    def click_content_major(self):
        """点击院系详情页的专业名称"""
        self.click("xpath->//tbody[@class='professionalDetailInfoTable_body']/tr[1]//a[@class='major']")

#左侧菜单

    def get_leftmenu_title(self):
        """获取左侧一级菜单名"""
        return self.get_text("xpath->//span[@class='side_bar_tips']")

    def get_left_secmenu(self,num=1):
        """获取左侧二级菜单名"""
        return self.get_text("xpath->//ul[@class='side_content_container']/li[%s]//span[@class='side_tips']" % num)

    def click_left_secmenu(self,num=1):
        """点击左侧二级菜单名"""
        self.click("xpath->//ul[@class='side_content_container']/li[%s]/a" % num)

    def get_left_thrmenu(self,num1,num2):
        """获取左侧三级菜单名"""
        return self.get_text("xpath->//ul[@class='side_content_container']/li[%s]//li[%d]/a" % (num1,num2))

    def click_left_thrmenu(self,num1,num2):
        """点击左侧三级菜单名"""
        self.click("xpath->//ul[@class='side_content_container']/li[%s]//li[%d]/a" % (num1,num2))

#文章列表
    def get_li_article_title(self,num=1):
        """获取文章列表文章标题"""
        return self.get_text("xpath->//div[@class='subList_content_msg']//li[%s]//span[@class='title']" % num)

    def click_li_article_title(self,num=1):
        """点击文章列表文章标题"""
        self.click("xpath->//div[@class='subList_content_msg']//li[%s]/a" % num)

    def click_btn_next(self):
        """点击下一页"""
        self.click("xpath->//a[@class='icon-next']")

    def click_btn_prev(self):
        """点击上一页"""
        self.click("xpath->//a[@class='icon-prev']")

    def click_pages_text(self,num):
        """点击页码"""
        self.click("xpath->//a[@href='javascript:toPage(%s)']" % num)

    def get_page_class_text(self,num):
        """获取页码元素信息,是否有 page_active """
        class_text=self.get_attribute("xpath->//a[@href='javascript:toPage(%s)']" % num,'class')
        class_text=class_text.split(" ")[1].strip()
        return class_text

#右侧悬浮栏
    def click_right_robot(self):
        """点击右侧机器人"""
        self.click("xpath->//div[@class='rightMode_robot']")

    def click_right_enrol(self):
        """点击右侧招录公告"""
        self.click("xpath->//div[@class='v3rightMode_book01']")

    def click_right_vedio(self):
        """点击视频在线"""
        self.click("xpath->//div[@class='v3rightMode_book02']")

    def click_right_picture(self):
        """点击校园风采"""
        self.click("xpath->//div[@class='v3rightMode_book03']")
#新开页面
    def have_WX_qrcode(self):
        """是否显示二维码"""
        return self.element_exist("xpath->//img[@class='qrcode lightBorder']")

    def have_message(self):
        """是否存在留言"""
        return self.element_exist("xpath->//a[@class='online_message active']")

#专业简介

    def click_major(self):
        """点击专业名称"""
        self.click("xpath->//a[text()=' 金融学(国际金融与市场)']")

    def click_department(self):
        """点击院系名称"""
        self.click("xpath->//a[text()='国际经济贸易学院']")
    '''
#院系设置
    def click_major_from_department(self,num=1):
        """点击专业名称"""
        self.click("xpath->//tbody[@class='facultyInfoTable_body']/tr[%s]//a[@class='major']" % num)

    def click_department_from_department(self):
        """点击院系名称"""
        self.click("xpath->//tbody[@class='facultyInfoTable_body']/tr[1]//a[@class='departId']")
    '''

    #（附加数据的表格）
    def click_enrollment_plan_title(self):
        """点击文章列表招生计划"""
        self.click("xpath->//span[text()='招生计划']")

    def get_additional_data_title(self):
        """获取招生计划页面信息"""
        return self.get_text("xpath->//li[@class='cur g-dropDownList drop-dwon']")

    def get_additional_data_title2(self):
        """获取招生计划页面信息"""
        return self.get_text("id->major-tab")

    def click_major_admission_title(self):
        """点击文章列表专业录取"""
        self.click("xpath->//span[text()='专业录取']")

    def click_school_admission_title(self):
        """点击文章列表学校录取"""
        self.click("xpath->//span[text()='学校录取']")

    def get_school_admission_title(self):
        """获取学校录取信息"""
        return self.get_text("xpath->//tr[@class='g-tbl-h-head']/th")

    def can_see_tab(self):
        """招生计划表格可见"""
        return self.element_exist("xpath->//div[@class='tab']")

    def click_major_plan(self):
        """点击专业历年招生计划"""
        self.click("id->major-tab")

    def click_school_plan(self):
        """点击学校历年招生计划"""
        self.click("xpath->//li[@class='cur g-dropDownList drop-dwon']")

    def can_see_major(self):
        """专业选择框可见"""
        return self.element_exist("xpath->//select[@id='majorName']")

    def click_major_admission(self):
        """点击单个专业录取"""
        self.click("id->major-tab")

    def click_year_admission(self):
        """点击各年度专业录取"""
        self.click("xpath->//li[@class='cur g-dropDownList drop-dwon']")

#填报参考
    def type_point(self,num=600):
        """输入分数"""
        self.type("xpath->//input[@name='preScore']",num)

    def click_analysis_reference(self):
        """点击分析参考"""
        self.click("id->referBtn")

    def can_see_analysis_result(self):
        """结果可见"""
        return self.element_exist("id->enrollForecast")