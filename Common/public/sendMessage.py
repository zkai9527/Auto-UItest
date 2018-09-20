__author__ = 'Administrator'
import requests
class SendMessagePage():

    def send_message(self,message):
        url='http://testadmin.zhinengdayi.com/weixin/api/common/sendMobileNotification'
        data={"mobiles":'18627128725',"templateId":'3115089',"params":message}
        s=requests.get(url,data)
        print(s)



if __name__ == '__main__':
    SendMessagePage().send_message("这是测试数据,系统异常，请及时处理")