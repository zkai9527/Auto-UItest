#encoding: utf-8
from Common.public.basepage import BasePage


class Home_page(BasePage):

    def into_3_1_homepage(self, url="http://zhinengdayi.com/gzcs"):
        self.open(url)
        self.wait(2)

#header登录注册模块
    def click_loginbtn(self):
        """点击登录"""
        self.click("xpath->//span[@class='tips02']")
        self.wait(1)

    def click_WXloginbtn(self):
        """点击微信登录"""
        self.click("xpath->//span[@class='icon-weChat']")

    def click_QQloginbtn(self):
        """点击QQ登录"""
        self.click("xpath->//span[@class='icon-qq']")

    def get_nickname(self):
        """获取用户名"""
        return self.get_text("xpath->//span[@class='fast_login_msg']")

#搜索框
    def type_search_text(self):
        """搜索框中输入搜索内容"""
        self.type("xpath->//input[@class='search_import']","奖助政策")

    def click_search_icon(self):
        """点击搜索按钮"""
        self.click("xpath->//i[@class='comicon-search']")

#headerlogo
    def logo_v3_1_visibility(self):
        """logo显示3.1 7.0 7.1 7.2"""
        return self.element_exist("xpath->//img[@class='school_logo']")

    def logo_v3_2_visibility(self):
        """logo显示3.2  4.0  4.1"""
        return self.element_exist("id->school-logo")

    def logo_v5_0_visibility(self):
        """logo显示"""
        return self.element_exist("xpath->//img[@class='header_logo']")

    def logo_v9_0_visibility(self):
        """logo显示"""
        return self.element_exist("xpath->//div[@class='logo fl']")

    def banner_visibility(self):
        """bannner图可见"""
        return self.element_exist("xpath->//div[@class='banner']")

#导航栏
    def move_to_Nav(self,num=1):
        """移动到导航栏菜单"""
        self.move_to_element("xpath->//ul[@class='first_nav']/li[%s]" % num)

    def click_Nav_Menu(self, num=1):
        """点击菜单"""
        self.click("xpath->//ul[@class='first_nav']/li[%s]" % num)

    def get_Nav_Menu(self, num=1):
        """获取导航栏菜单名"""
        return self.get_text("xpath->//ul[@class='first_nav']/li[%s]//a[@class='first_msg']" % num)

    def get_Nav_articles(self, num=1):
        """获取该菜单下文章标题"""
        return self.get_text("xpath->//ul[@class='first_nav']/li[1]//ul/li[%s]" % num)

    def click_Nav_articles(self, num=1):
        """点击文章"""
        self.click("xpath->//ul[@class='first_nav']/li[1]//ul/li[%s]" % num)

    def click_Nav_major(self):
        self.click("xpath->//span[text()='专业简介']")


#自定义项
    def get_custom_Link(self):
        """获取自定义项的link"""
        return self.get_attribute("xpath->//span[text()='网上报名系统']//parent::a","link")

    def click_custom(self):
        """点击自定义项"""
        self.click_text("网上报名系统")

#招录公告
    def click_enrol_title(self):
        """点击模块名"""
        self.click("xpath->//span[@class='tips']")

    def get_enrol_title(self):
        """获取模块名"""
        return self.get_text("xpath->//span[@class='tips']")

    def get_enrol_articles(self):
        """获取第一篇文章的文章名"""
        return self.get_text("xpath->//div[@class='hot_message_content']//li[1]//span[@class='hot_message_title']")

    def click_Enroll_articles(self):
        """点击第一篇文章"""
        self.click("xpath->//div[@class='hot_message_content']//li[1]//span[@class='hot_message_title']")

#右侧悬浮按钮
    def click_right_robot(self):
        """点击机器人图标"""
        self.click("xpath->//div[@class='floatItem01']")

    '''删除弹框，直接跳转登录界面
    def robot_login(self):
        """机器人弹框点击登录"""
        self.click("xpath->//div[@class='contents']//span[text()=' 登录']")


    def robot_register(self):
        """机器人弹框点击注册"""
        self.click("xpath->//div[@class='contents']//span[text()='注册']")

    '''

    def move_to_rightQrcode(self):
        """鼠标移动到右侧二维码图标"""
        self.move_to_element("xpath->//div[@class='floatItem02']")

    def can_to_see_qrcode(self):
        """二维码悬浮框可见"""
        return self.element_exist("xpath->//img[@class='erweima']")

    def click_right_hot(self):
        """点击右侧HOT图标"""
        self.click("xpath->//div[@class='floatItem03 usericon-webicon-70']")

#快捷入口
    def move_to_Quick(self):
        """移动到第一个分类"""
        self.move_to_element("xpath->//div[@class='hot_quick_container']/ul/li[1]/div[@class='hot_quick_item']")

    def get_quick_name(self):
        """获取分类名"""
        return self.get_text("xpath->//div[@class='hot_quick_container']/ul/li[1]//span[@class='tips01']")

    def click_quicknav(self):
        """点击分类名"""
        self.click("xpath->//div[@class='hot_quick_container']/ul/li[1]//span[@class='tips01']")

    def get_quick_articles(self):
        """获取文章名"""
        return self.get_text("xpath->//div[@class='hot_quick_container']/ul/li[1]//ul[@class='itemList_msg']/li[1]")

    def click_quick_articles(self):
        """点击文章"""
        self.click("xpath->//div[@class='hot_quick_container']/ul/li[1]//ul[@class='itemList_msg']/li[1]")

    def click_quickmore(self):
        """点击更多按钮"""
        self.click("xpath->//div[@class='hot_quick_container']/ul/li[1]//a[@class='itemList_more']")

#招生快讯
    def get_Flash_nav(self):
        """获取快讯名"""
        return self.get_text("xpath->//a[@class='title active']")

    def click_Flash_nav(self):
        """点击分类名"""
        self.click("xpath->//a[@class='title active']")

    def get_Flash_articles(self):
        """获取文章名"""
        return self.get_text("xpath->//a[@class='title active']//following-sibling::div//a[@class='msg01']")

    def click_Flash_articles(self):
        """点击文章"""
        self.click("xpath->//a[@class='title active']//following-sibling::div//a[@class='msg01']")

    def move_to_second_Flash_nav(self):
        """移动到第二个分类"""
        self.move_to_element("xpath->//a[@class='title']")

#简章
    def click_rules_Nav(self):
        """点击简章名"""
        self.click("xpath->//div[@class='admissionBrochures_title_itemMsg']")

    def get_rules_article(self):
        """获取文章名"""
        return self.get_text("xpath->//div[@class='admissionBrochures_itemList']/ul/li[1]//div[@class='title01']")

    def click_rules_article(self):
        """点击文章"""
        self.click("xpath->//div[@class='admissionBrochures_itemList']/ul/li[1]//div[@class='title01']")

#视频在线
    def click_vedio_Nav(self):
        """点击标题"""
        self.click("xpath->//span[text()='视频在线']")

    def click_vedio_first(self):
        """点击视频"""
        self.click("xpath->//div[@class='videoList_item']/a[1]")

    def click_vedio_second(self):
        """点击视频"""
        self.click("xpath->//div[@class='videoList_item']/a[2]")

#智能咨询
    def click_robot_btn(self):
        """点击机器人按钮"""
        self.click("xpath->//a[@class='robot_btn']")

    '''
    def move_to_content(self):
        """弹框可见"""
        return self.element_exist("xpath->//div[@class='contents']")
    '''

    def move_to_phone(self):
        """移动到电话咨询"""
        self.move_to_element("xpath->//div[@class='robot_advisory']//li[1]")

    def get_phone_text(self):
        """获取咨询电话文本"""
        return self.get_text("xpath->//div[@class='robot_advisory']//li[1]//span[@class='msg01']")

    def move_to_email(self):
        """移动到电话咨询"""
        self.move_to_element("xpath->//div[@class='robot_advisory']//li[2]")

    def get_email_text(self):
        """获取邮箱文本"""
        return self.get_text("xpath->//div[@class='robot_advisory']//li[2]//span[@class='msg01']")

    def move_to_message(self):
        """移动到留言咨询图标"""
        self.move_to_element("xpath->//span[text()='留言咨询']")

    def click_message(self):
        """点击留言咨询"""
        self.click("xpath->//div[text()='点击进入留言咨询']")

#人物
    def get_teacher_firstArticle(self):
        """获取第一个文章名"""
        return self.get_text("xpath->//ul[@class='JQ-slide-content']/li[1]//span[@class='desc01']")

    def get_teacher_secondArticle(self):
        """获取第二个文章名"""
        return self.get_text("xpath->//ul[@class='JQ-slide-content']/li[2]//span[@class='desc01']")

    def move_and_click_teacher_firstArticle(self):
        """移动到第一篇文章并点击"""
        self.move_to_element("xpath->//ul[@class='JQ-slide-content']/li[1]//img")
        self.click("xpath->//ul[@class='JQ-slide-content']/li[1]//span[@class='more_btn']")

    def click_teacher_leftBtn(self):
        """点击左侧箭头"""
        self.click("xpath->//span[text()='‹']")

#故事
    def get_story_nav(self):
        """获取故事分类名"""
        return self.get_text("xpath->//div[@class='culture_title_content']/span")

    def click_story_nav(self):
        """点击分类名"""
        self.click("xpath->//div[@class='culture_title_content']/span")

    def get_story_articles(self):
        """获取第一篇文章名"""
        return self.get_text("xpath->//div[@class='culture_content']/span[@class='title01']")

    def click_story_articles(self):
        """点击第一篇文章"""
        self.click("xpath->//div[@class='culture_content']/span[@class='title01']")

    def get_story_secondArticles(self):
        """获取第二篇文章标题"""
        return self.get_text("xpath->//div[@class='culture_content']/div[@class='msg02']/ul/li[1]")

    def click_story_secondArticles(self):
        """点击第二篇文章"""
        self.click("xpath->//div[@class='culture_content']/div[@class='msg02']/ul/li[1]")

#校园风采
    def click_picture(self):
        """点击校园风采"""
        self.click("xpath->//div[@class='Scenery']")

#友情链接
    def click_friendlink(self):
        """点击友情链接"""
        self.click_text("1")

    def get_friendlick_href(self):
        """获取友情链接"""
        link=self.get_attribute("xpath->//div[@class='footer_msg_left01']/ul/li[2]/a","hreflink")

        if ":" not in link:
            return link

        else:
            link_l=link.split(":")[1].strip()
            return link_l