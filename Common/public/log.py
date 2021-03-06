#encoding=utf-8

import logging
import time
import os
from Common.public.projectPath import *

class Log:

    def __init__(self):
        self.log_name = os.path.join(Log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def mylog(self, level, message):

        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.log_name,'a',encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def debug(self,message):
        self.mylog('debug', message)

    def info(self,message):
        self.mylog('info', message)

    def warning(self,message):
        self.mylog('warning', message)

    def error(self,message):
        self.mylog('error', message)
