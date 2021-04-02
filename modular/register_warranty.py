#coding=utf-8
from public.Commonlib import Common
from public.rd_email_name import RD
from modular.register import Register


import time


class WarrantyAct(object):

    def __init__(self,dr):
        self.driver = dr
        self.elt = Common(self.driver)
        self.r_email = Register(self.driver)
        self.rd = RD(self.driver)



    def register_warranty(self,account,order_num):
        #注册延保
        try:
            WarrantyAct.register_submit(self,account,order_num)
            time.sleep(2)
            class_status = self.driver.find_element_by_xpath("//*[@id='__layout']/div/div").get_attribute("class")
            # print(class_status)
            if class_status == "thanks-for-rating":
                return "register success"
            else:
                return "register fail"
        except Exception as e:
            return e

    def login_warranty(self,email,order_num):
        #登录延保
        try:
            WarrantyAct.login_submit(self,email,order_num)
            time.sleep(2)
            class_status = self.driver.find_element_by_xpath("//*[@id='__layout']/div/div").get_attribute("class")
            print(class_status)
            if class_status == "thanks-for-rating":
                return "login warranty success"
            else:
                return "login warranty fail"


        except Exception as e:
            return e

    def input_three_start(self):
        #订单评星
        try:
            self.elt.click('xpath','//*[@id="__layout"]/div/div/div[2]/div[3]/ul/li[3]/div/div[1]/i')
            time.sleep(1)
            #点击Next Step
            self.elt.click('xpath','//*[@id="__layout"]/div/div/div[2]/button')
            time.sleep(1)
            title_start = self.elt.get_text('xpath','//*[@id="__layout"]/div/div/div[2]/p[1]')
            if title_start == "Thank you for rating our product!":
                return  "input three start success"
            else:
                return  "input three start fail"

        except Exception as e:
            return e

    def input_five_start(self):
        #评五星
        try:
            self.elt.click('xpath', '//*[@id="__layout"]/div/div/div[2]/div[3]/ul/li[5]/div/div[1]/i')
            time.sleep(1)
            # 点击Next Step
            self.elt.click('xpath', '//*[@id="__layout"]/div/div/div[2]/button')
            time.sleep(1)
            five_start_text = self.elt.get_text('xpath','//*[@id="__layout"]/div/div/div[2]/div[1]/h3')
            if "Share your review with us and get another" in five_start_text:
                #点击share to get xxx point
                self.elt.click('xpath','//*[@id="__layout"]/div/div/div[2]/ul/li/div[2]/div[1]/div/button')
                #获取当前句柄
                WarrantyAct.get_handle(self)
                time.sleep(2)
                #判断是否进入RV留评页面
                rv_text = self.elt.get_text('xpath','//*[@id="__layout"]/div/div/div[2]/ul/li/div[2]/form/div[1]/span/div/span/button/span')
                if rv_text == "Upload File":
                    #输入亚马逊链接
                    self.elt.input_send('xpath','//*[@id="__layout"]/div/div/div[2]/ul/li/div[2]/form/div[2]/input',
                                        'https://www.amazon.com/review/mpow_ui_test')
                    time.sleep(1)
                    #js下拉滚动
                    js = "window.scrollTo(0,500)"
                    self.driver.execute_script(js)
                    time.sleep(1)
                    #点击submit
                    self.elt.click('xpath','//*[@id="__layout"]/div/div/div[2]/div[2]/button')
                    time.sleep(3)
                    # 获取最后一个句柄
                    WarrantyAct.get_handle(self)
                    print(self.driver.title)
                    print(self.driver.current_url)
                    #判断是否提交rv成功
                    thanks_text = self.elt.get_text('xpath','//*[@id="__layout"]/div/div/div[2]/div/p')
                    if thanks_text == "All MPOW members will benefit from your sharing. Much appreciated!^_^":
                        return  "warranty and submit rv success"
                    else:
                        return  "warranty and submit rv fail"
                else:
                    return "not upload file text"




            else:
                return "not start pages"


        except Exception as e:
            return e

    def get_handle(self):
        #切换至当前句柄
        try:
            # 获取当前句柄
            now_handle = self.driver.current_window_handle
            print(now_handle)
            all_handles = self.driver.window_handles
            if len(all_handles) > 2:
                print(all_handles)
                print(all_handles[-1])
                self.driver.switch_to_window(all_handles[-1])
                time.sleep(1)
            else:
                for handle in all_handles:
                    if handle != now_handle:
                        print(handle)
                        self.driver.switch_to_window(handle)
                        time.sleep(1)
        except Exception as e:
            return  e


    def login_submit(self,email,order_num):
        #登录延保流程

        #点击login

        self.elt.click('xpath','//*[@id="__layout"]/div/div/div[1]/div[2]/div/div[1]/div[2]')
        time.sleep(1)

        #订单号
        self.elt.input_send("xpath", "//*[@id='__layout']/div/div/div[1]/div[2]/div/form/div[1]/div[2]/div/span/input",
                            order_num)


        self.elt.input_send('xpath', '//*[@id="__layout"]/div/div/div[1]/div[2]/div/form/div[2]/div[2]/div/span/input', email)
        #密码
        password = self.rd.return_password()
        self.elt.input_send('xpath','//*[@id="__layout"]/div/div/div[1]/div[2]/div/form/div[3]/div[2]/div/span/input',password)
        # SUBMIT
        self.elt.click('xpath', '//*[@id="__layout"]/div/div/div[1]/div[2]/div/div/button')
        time.sleep(5)


    def register_submit(self,account,order_num):
        #注册延保
        # 点击new user
        self.elt.click("xpath", "//*[@id='__layout']/div/div/div[1]/div[2]/div/div[1]/div[1]")
        time.sleep(1)
        # self.driver.switch_to.frame(self.driver.find_element_by_id('myiframe'))
        # 订单号                      //*[@id="app"]/div/div[1]/div[2]/div/form/div[1]/div[2]/div/span/input
        self.elt.input_send("xpath", "//*[@id='__layout']/div/div/div[1]/div[2]/div/form/div[1]/div[2]/div/span/input",
                            order_num)
        time.sleep(0.5)


        self.elt.input_send('xpath', '//*[@id="__layout"]/div/div/div[1]/div[2]/div/form/div[2]/div[2]/div/span/input', account)
        # first name  last name
        first_name = "sunny"
        last_name = "hong"
        self.elt.input_send("xpath",'//*[@id="__layout"]/div/div/div[1]/div[2]/div/form/div[3]/div[1]/div[2]/div/span/input',first_name)
        self.elt.input_send("xpath",
                            '//*[@id="__layout"]/div/div/div[1]/div[2]/div/form/div[3]/div[2]/div/div/span/input',
                            last_name)

        # 密码
        password = self.rd.return_password()
        self.elt.input_send('xpath', '//*[@id="__layout"]/div/div/div[1]/div[2]/div/form/div[4]/div[2]/div/span/input', password)
        # SUBMIT
        self.elt.click('xpath', '//*[@id="__layout"]/div/div/div[1]/div[2]/div/div/button')
        time.sleep(5)

    def clost_pop_up(self):
        #关闭首页弹框
        try:
            class_status = self.driver.find_element_by_id("Modalnewsletter").get_attribute("class")
            # print(class_status)
            if class_status == "modal fade show":
                js = "document.getElementById('Modalnewsletter').setAttribute('class','modal fade')"
                self.driver.execute_script(js)
                self.driver.refresh()
                time.sleep(1)
        except Exception as e:
            print(e)


