#encoding: utf-8
import xlrd
from Common.public.log import Log
from Common.public.projectPath import *


class GetData():

    def __init__(self):
        self.log = Log()

    def Exceldata(self,path):
        #self.log.info("测试数据地址:"+path)
        workbook=xlrd.open_workbook(path)
        sheet_obj=workbook.sheet_by_index(0)
        data_list=[]
        nrow=sheet_obj.nrows
        for i in range(1,nrow):
            row_value=sheet_obj.row_values(i)
            data_list.append(row_value)
        return data_list

#测试代码
# H = GetData().Exceldata("D:\\python_project\\Project\\UI-Automation\\Common\\conf\\Online_school_config.xls")
# print(H)
