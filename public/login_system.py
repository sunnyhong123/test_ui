#coding=utf-8
from public import Commonlib,readxlsx
import time

class LoginSystem(object):
    def __init__(self,dr):
        self.driver = dr
        self.elt = Commonlib.Common(self.driver)
        self.date = readxlsx.GetDate(self.driver)
        #账号密码信息路经
        self.path = "\\databases\\usermsg.txt"
        #正确登录邮箱路经
        self.e_path = "\\databases\\login_email.txt"
        #随机生成邮箱路经
        self.r_e_path = "\\databases\\rd_email.txt"
        #延保邮箱路经
        self.w_path = "\\databases\\warranty_email.txt"

    def Choice_system(self, ope_type,num):
        try:
            #选择登录不同的官网会员系统
            if ope_type == "mpow":
                return LoginSystem.login_mpow(self,num)
            elif ope_type == "victsing":
                return  LoginSystem.login_victsing(self)
            elif ope_type == "holife":
                return  LoginSystem.login_holife(self)
            elif ope_type == "ikich":
                return  LoginSystem.login_ikich(self,num)
            else:
                print("choice system error...")

        except Exception as e:
            return e

    def login_ikich(self,num):
        global get_email
        try:
            #点击请选择品牌官网
            self.elt.click("xpath","//*[@id='app']/div/div/form/div[2]/div/div/div[1]/input")
            time.sleep(0.5)
            self.elt.click("xpath",'/html/body/div[2]/div[1]/div[1]/ul/li[4]/span')
            time.sleep(0.5)
            #username
            read_username = self.date.read_doc(self.path).split(",")[0]
            print(read_username)
            #password
            read_password = self.date.read_doc(self.path).split(",")[1]
            print(read_password)
            self.elt.input_send("name","username",read_username)
            self.elt.input_send("name", "password", read_password)
            #点击Login
            self.elt.click("xpath",'//*[@id="app"]/div/div/form/button/span')
            time.sleep(2)
            username_msg = self.elt.get_text("xpath","//*[@id='app']/div/div[2]/section/div/div[1]")
            ikich_msg = self.elt.get_text("xpath","//*[@id='app']/div/div[2]/section/div/div[2]/span")
            if username_msg == "用户名: alice_huang":
                if ikich_msg == "ikich":
                    print("login success ...")
                    #判断是否是24小时免费邮箱或者随机生成的无效邮箱
                    #"1" ==> 24小时有效邮箱
                    #"2" ==> 随机生成无效邮箱
                    if num == "1":
                        # 获取注册用户邮箱
                        get_email = self.date.read_doc(self.e_path)
                        print(get_email)
                    elif num == "2":
                        get_email =self.date.read_doc(self.r_e_path)
                        print(get_email)
                    delete_email_is_true = LoginSystem.delete_email(self,get_email)
                    if delete_email_is_true[0] is True:
                        return  delete_email_is_true[1]
                    else:
                        self.elt.get_screenshot()
                        return  delete_email_is_true[1]
                else:
                    self.elt.get_screenshot()
                    return  "login system error ..."
            else:
                self.elt.get_screenshot()
                return  "username error..."
        except Exception as e:
            return e

    def delete_email(self,get_email):
        #删除用户
        try:

            class_status = self.driver.find_element_by_xpath("//div[@id='app']/div").get_attribute("class")


            if "hideSidebar" in class_status:
                self.driver.find_element_by_class_name("hamburger").click()
                time.sleep(1)
            elif "openSidebar" in class_status:
                pass
            else:
                raise Exception("not found element!")


            #点击会员               //*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/div

            self.elt.click("class_name",'el-submenu__title')
            time.sleep(0.5)
             #         //*[@id="app"]/div/div[1]/div/div[1]/div/ul/div[2]/li/ul/div[1]/a/li
            self.elt.click("css",'#app > div > div.sidebar-container > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(2) > li > ul > div:nth-child(1) > a > li')
            time.sleep(2)

            #判断注册邮箱是否在会员列表中 //*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/input
            self.elt.input_send('xpath','//*[@id="app"]/div/div[2]/section/div/div[1]/form/div[1]/div/div/input',get_email)

            print(get_email)
            time.sleep(1)  #
            self.elt.click('xpath','//section[@class="app-main"]/div/div[1]/form/div[6]/div/button')

            time.sleep(2)
            #判断查询列表是否为空                     //*[@id="app"]/div/div[2]/section/div/div[3]/div[4]/div[2]/table/tbody/tr
            email_list = self.elt.common("elements",'//*[@id="app"]/div/div[2]/section/div/div[3]/div[4]/div[2]/table/tbody/tr')
            print(email_list)
            if len(email_list) > 0:
                email_msg = self.elt.get_text('xpath','//*[@id="app"]/div/div[2]/section/div/div[3]/div[3]/table/tbody/tr/td[2]/div/span')
                if get_email == email_msg:
                    class_status = self.driver.find_element_by_xpath("//div[@id='app']/div").get_attribute("class")


                    if "hideSidebar" in class_status:
                        self.driver.find_element_by_class_name("hamburger").click()
                        time.sleep(1)
                    elif "openSidebar" in class_status:
                        pass
                    else:
                        raise Exception("not found element!")


                    #执行删除操作
                    self.elt.click('css','#app > div > div.sidebar-container > div > div.scrollbar-wrapper.el-scrollbar__wrap > div > ul > div:nth-child(2) > li > ul > div:nth-child(3) > a > li')
                    time.sleep(1)
                    self.elt.input_send('xpath','//*[@id="app"]/div/div[2]/section/div/div/form/div[1]/div/div/textarea',get_email)
                    #点击删除按钮
                    self.elt.click('xpath','//*[@id="app"]/div/div[2]/section/div/div/form/div[2]/div/button[1]/span')
                    time.sleep(1)
                    self.elt.click('xpath','/html/body/div[2]/div/div[3]/button[2]/span')
                    time.sleep(2)
                    delete_msg = self.elt.get_text('xpath','/html/body/div[3]/p')
                    if delete_msg == "删除成功":
                        return True , "delete email success"
                    else:
                        self.elt.get_screenshot()
                        return  False ,"delete email fail"
                else:
                    self.elt.get_screenshot()
                    return  "get email != email msg ..."
            else:
                self.elt.get_screenshot()
                return  "search get email is null"
        except Exception as e:
            raise Exception(e)

    def login_mpow(self,num):
        global get_email
        try:
            # 点击请选择品牌官网
            self.elt.click("xpath", "//*[@id='app']/div/div/form/div[2]/div/div/div[1]/input")
            time.sleep(0.5)
            self.elt.click("xpath", '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')
            time.sleep(0.5)
            # username
            read_username = self.date.read_doc(self.path).split(",")[0]
            print(read_username)
            # password
            read_password = self.date.read_doc(self.path).split(",")[1]
            print(read_password)
            self.elt.input_send("name", "username", read_username)
            self.elt.input_send("name", "password", read_password)
            # 点击Login
            self.elt.click("xpath", '//*[@id="app"]/div/div/form/button/span')
            time.sleep(2)
            login_text = self.elt.get_text("xpath", "//*[@id='app']/div/div[2]/div/div/div[2]/span/span/span[1]/span")
            if login_text == "仪表盘":
                print("login success ...")
                # 判断是否是24小时免费邮箱或者随机生成的无效邮箱
                # "1" ==> 24小时有效邮箱
                # "2" ==> 随机生成无效邮箱
                # "3" ==> 延保成功邮箱
                if num == "1":
                    # 获取注册用户邮箱
                    get_email = self.date.read_doc(self.e_path)
                    print(get_email)
                elif num == "2":
                    get_email = self.date.read_doc(self.r_e_path)
                    print(get_email)
                elif num == "3":
                    get_email = self.date.read_doc(self.w_path)
                delete_email_is_true = LoginSystem.delete_email(self, get_email)
                if delete_email_is_true[0] is True:
                    return delete_email_is_true[1]
                else:
                    self.elt.get_screenshot()
                    return delete_email_is_true[1]
            else:
                self.elt.get_screenshot()
                return "login system error ..."

        except Exception as e:
            raise Exception(e)

    def login_victsing(self):
        pass

    def login_holife(self):
        pass

