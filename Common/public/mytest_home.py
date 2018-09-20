#encoding=utf-8
import unittest
from Common.public.log import Log
from Common.public.driver import Browser
from Common.public.readconfig import ReadConfig
from Common.public.projectPath import *

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    @classmethod
    def setUpClass(self):
        self.logger = Log()
        self.verificationErrors = []
        self.logger.info('############################### START ###############################')
        browser = ReadConfig().read_config(conf_path,"BROWSER","browser")
        self.dr = Browser(browser).driver()
        self.dr.maximize_window()

    @classmethod
    def tearDownClass(self):
        self.dr.close()
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')
