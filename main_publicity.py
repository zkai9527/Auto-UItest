__author__ = 'Administrator'
import unittest
from Common.public.projectPath import *

def run():
    test_dir = TestCases_path+'/publicity'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
    runner=unittest.TextTestRunner()
    runner.run(suite)

if __name__=='__main__':
    run()

