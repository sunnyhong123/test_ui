#coding=utf-8

from public.Commonlib import Common
from public.rd_email_name import RD
import time


class Subscirbe():

    def __init__(self,dr):
        self.driver = dr
        self.elt = Common(self.driver)
        self.rm = RD(self.driver)

    def subscribe_success(self):
        #订阅流程
        subscribe_value = self.elt.get_text("xpath",'//*[@id="Modalnewsletter"]/div/div/div[2]/div/div/div/div[1]/div[3]')
        print(subscribe_value)
        if subscribe_value:
            #输入邮箱号
            email =self.rm.rd_email()
            print(email)
            time.sleep(0.5)   #//*[@id="Modalnewsletter"]/div/div/div[2]/div/div/div/div[2]/div/form/div/input[2]
            self.elt.input_send("xpath",'//*[@id="Modalnewsletter"]/div/div/div[2]/div/div/div/div[2]/div/form/div/input[2]',email)
            #点击JOIN US
            self.elt.click('xpath','//*[@id="Modalnewsletter"]/div/div/div[2]/div/div/div/div[2]/div/form/div/div')
            time.sleep(3)
            success_text = self.elt.get_text('xpath','//*[@id="ModalSubsribeGood"]/div/div/div[2]/div/span')
            if success_text == "You have successfully subscribed!":
                #关闭提示弹框
                self.elt.click('xpath','//*[@id="ModalSubsribeGood"]/div/div/div[1]/button')
                return "subscribe success"
            else:
                return "subscribe fail"

