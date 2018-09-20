__author__ = 'Administrator'
from pyfetion.fetion import Fetion
import os

def SendSMS(sms):
    myphone = 'xxxxxx'
    mypwd = 'oooooooooo'
    tophone = 'oxoxoxoxoxox'

    fetion = PyFetion(myphone,mypwd,'TCP')
    fetion.login(FetionHidden)
    print ('send to '+tophone)
    fetion.send_sms(sms,tophone,True)
    print('OK')

    fetion.logout()
    return True

msg = "hello world"
SendSMS(msg)
print ('OK!!!')
