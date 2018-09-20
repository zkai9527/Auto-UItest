__author__ = 'Administrator'
#encoding: utf-8
import os
import configparser

cf = configparser.ConfigParser()

#获取当前路径
config_file_path = os.path.split(os.path.realpath(__file__))[0]
config_file_path = os.path.split(os.path.realpath(config_file_path))[0]

cf.read(config_file_path+"\\conf\\config.conf")
file_path = cf["DIRECTORY"]["directory"]

#html报告路径
HtmlReport_path = os.path.join(file_path, "report\\HtmlReport")
#测试用例路径
TestCases_path = os.path.join(file_path, "TestCases")
#附加数据用例路径
Additional_path = os.path.join(file_path, "TestCases\\publicity\\Additional_data")
#日志路径
Log_path = os.path.join(file_path, "report\\Logs")
#截图路径
Image_path = os.path.join(file_path, "report\\Images")
#配置文件路径
conf_path = os.path.join(file_path, "Common\\conf\\config.conf")
#学校官网配置文件路径
school_path = os.path.join(file_path, "Common\\conf\\Online_school_config.xls")


