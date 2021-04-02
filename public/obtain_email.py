#coding=utf-8
from public import Commonlib,readxlsx
import time

class ObtainEmail(object):
    def __init__(self,dr):
        self.driver = dr
        self.elt = Commonlib.Common(self.driver)
        self.date = readxlsx.GetDate(self.driver)
        #邮件路经
        self.path = "\\databases\\email.txt"

    def obtainemail(self):
        #打开 免费邮箱 http://24mail.chacuo.net/enus
        try:
            time.sleep(5)
            #获取邮件个数文本mails
            text = self.elt.get_text("id","mail_cur_total")
            if text == "0":
                #获取免费邮箱
                while True:
                    mail_cur_name = self.elt.common("id","mail_cur_name").get_attribute("value")
                    #若邮箱为空白 刷新页面
                    if mail_cur_name == "":
                        self.driver.refresh()
                        time.sleep(2)
                    else:
                        break
            else:
                #点击A mailbox
                self.elt.click("xpath","//*[@id='main']/div[2]/div[1]/div/div[1]/div[1]/input[2]")
                mail_cur_name = self.elt.common("id", "mail_cur_name").get_attribute("value")

            #读取邮箱
            read_mail = self.date.read_doc(self.path)
            #保存邮箱
            self.date.save_doc(self.path,read_mail.replace(read_mail,mail_cur_name))
            after_read_mail = self.date.read_doc(self.path)
            if read_mail != after_read_mail:
                return  "obtain email success"
            else:
                self.elt.get_screenshot()
                return  "obtain email fail"

        except Exception as e:
            return e



