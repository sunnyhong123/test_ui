#coding=utf-8
from public import Commonlib,log,rd_email_name
import random,time
from selenium.webdriver.support.ui import Select
from datetime import datetime

class MyAccount(object):
    def __init__(self,dr):
        self.driver = dr
        self.elt = Commonlib.Common(self.driver)
        self.logger = log.Mylog("Mpow").getlog()
        self.rd = rd_email_name.RD(self.driver)

    def my_account(self):
        #submit 个人信息页面
        try:
            submit_is_true = MyAccount.return_submit_msg(self)
            if submit_is_true[0] is True:
                self.logger.info("return My Account msg : %s" %submit_is_true[1])
                return submit_is_true[1]
            else:
                self.logger.error("return My Account error msg : %s" % submit_is_true[1])
                self.elt.get_screenshot()
                return submit_is_true[1]

        except Exception as e:
            return e

    def return_submit_msg(self):
        #填写个人信息
        try:
            #判断用户是否已经提交过个人信息
            update_profile = self.elt.get_text('xpath','//*[@id="__layout"]/div/div/div/div/div[2]/div/div/button/span')
            if update_profile != "Edit Profile":
                time.sleep(2)
                # self.driver.switch_to.frame(self.driver.find_element_by_id("myiframe"))
                #user name last name
                first_name =self.rd.rd_name()
                print(first_name)
                last_name = self.rd.rd_name()
                print(last_name)
                self.elt.input_send("xpath",'//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[2]/div[1]/div/div[2]/div/span/input',first_name)
                self.elt.input_send("xpath", '//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[2]/div[2]/div/div[2]/div/span/input', last_name)

                #随机选择country
                self.elt.click("xpath", '//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[3]/div[1]/div/div[2]/div/span/div/div/span')
                time.sleep(0.5)  #/html/body/div[24]/div/div     /html/body/div[22]/div/div
                MyAccount.rd_country_gender_birthday(self,23)
                time.sleep(1)

                #随机选择city
                city = self.rd.return_city()
                self.elt.input_send("xpath",'//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[3]/div[2]/div/div[2]/div/span/input',city)

                # #删除日历控件属性readonly
                # js = "document.getElementById('birthday').removeAttribute('readonly');"
                # self.driver.execute_script(js)
                #
                # time.sleep(0.5)
                # now = datetime.now().strftime("%Y-%m-%d")
                # print(now)
                # mm =int(now.split("-")[1])
                # dd = int(now.split("-")[2])
                # yy = random.randrange(0,5)
                # #月份
                # self.elt.click("xpath",'//*[@id="new-account-form-month"]/span')
                # time.sleep(0.5)
                # self.elt.click("xpath",'//*[@id="new-account-form-month"]/ul/li[%d]'%mm)
                # #天
                # time.sleep(0.5)
                # self.elt.click("id", 'new-account-form-day')
                #
                # time.sleep(0.5)
                # self.elt.click("xpath", '//*[@id="new-account-form-day"]/ul/li[%d]' % dd)
                # #年
                # time.sleep(0.5)
                # self.elt.click("id", 'new-account-form-year')
                # time.sleep(0.5)
                # self.elt.click("xpath", '//*[@id="new-account-form-year"]/ul/li[%d]' % yy)
                # time.sleep(0.5)
                # self.elt.get_screenshot()

                #Birthday
                #MM
                self.elt.click("xpath",'//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[4]/div[1]/div/div[2]/div/span/div/div[1]/div/div/span')
                time.sleep(0.5)
                self.elt.click("xpath",'/html/body/div[24]/div/div/div/ul/li[1]')
                time.sleep(0.5)
                #DD
                self.elt.click('xpath','//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[4]/div[1]/div/div[2]/div/span/div/div[2]/div/div/span')
                time.sleep(0.5)   #/html/body/div[24]/div/div  /html/body/div[25]/div/div
                self.elt.click('xpath','/html/body/div[25]/div/div/div/ul/li[1]')
                time.sleep(0.5)
                #YYYY    /html/body/div[26]/div/div
                self.elt.click('xpath','//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[4]/div[1]/div/div[2]/div/span/div/div[3]/div/div/span')
                time.sleep(0.5)
                self.elt.click('xpath','/html/body/div[26]/div/div/div/ul/li[1]')

                #随机选择性别Gender  /html/body/div[24]  /html/body/div[23]/div/div
                self.elt.click('xpath','//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[4]/div[2]/div/div[2]/div/span/div/div/span/i')
                MyAccount.rd_country_gender_birthday(self,24)

                #滑动滚动条
                js = "window.scrollTo(0,200)"
                time.sleep(0.5)
                self.driver.execute_script(js)

                time.sleep(0.5)
                #submit
                self.elt.click("xpath",'//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[5]/button')

                time.sleep(3)
                submit_msg = self.elt.get_text("xpath",'//*[@id="__layout"]/div/div/div/div/div[2]/div/form/div[6]')
                # Your information has been saved successfully.
                if submit_msg == "Complete your profile to get 50 points.":
                    return  True ,"submit success"
                else:
                    return  False , "submit fail"
            else:
                return  False,"profile is update"
        except Exception as e:
            self.elt.get_screenshot()
            return e
    def rd_country_gender_birthday(self,num):
        #随机选择国家或者性别   /html/body/div[22]/div/div /html/body/div[23]/div/div  /html/body/div[23]
        try:
            ul_list = []
            ul = self.driver.find_elements_by_xpath('/html/body/div[%d]/div/div/div/ul/li'%num)
            for i in ul:
                print(i.text)
                ul_list.append(i.text)
            rd_country_num = random.randrange(1, len(ul_list))
            self.elt.click("xpath", '/html/body/div[%s]/div/div/div/ul/li[%s]' % (num,rd_country_num))

        except Exception as e:
            return e

    def rd_select(self,id_value):
        try:
            country_list = []
            elements = self.elt.common("elements", "//*[@id='%s']/ul" %id_value)
            for options in elements:
                country_list.append(options.get_attribute("value"))
            rd_num = country_list[random.randrange(0, len(country_list))]
            Select(self.elt.common("id", id_value)).select_by_value(rd_num)

        except Exception as e:
            return e