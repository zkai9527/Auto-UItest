__author__ = 'Administrator'
import configparser
#from Common.public.projectPath import *


class ReadConfig:

    def read_config(self, path, section, option):
        cf = configparser.ConfigParser()
        cf.read(path)
        return cf[section][option]

#test coding
#print(ReadConfig().read_config(conf_path,"RECVER","recver"))