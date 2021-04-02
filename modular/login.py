#coding=utf-8
from public import Commonlib,log,rd_email_name,readxlsx
import time

class Login(object):
    def __init__(self,dr):
        self.driver = dr
        self.elt = Commonlib.Common(self.driver)
        self.logger = log.Mylog("Mpow").getlog()
        self.login_msg = rd_email_name.RD(self.driver)
        #正常登录==注册邮箱路经
        self.path = "\\databases\\login_email.txt"
        self.date = readxlsx.GetDate(self.driver)

    def test_login(self):
        try:
            #正常登录
            email = self.login_msg.return_login_email()[0]
            # print(email)
            password = self.login_msg.return_login_email()[1]
            # print(password)
            login_is_true = Login.return_login_result(self,email,password)
            if login_is_true[0] is True:
                self.logger.info("login msg : %s" %login_is_true[1])
                return login_is_true[1]
            else:
                self.logger.error("login error msg : %s" % login_is_true[1])
                self.elt.get_screenshot()
                return login_is_true[1]
        except Exception as e:
            self.logger.error("login exception msg : %s" % e)
            return e

    def test_email_null(self):
        #邮箱为空
        try:
            email = ""
            password = self.login_msg.return_login_email()[1]
            login_error_is_true = Login.return_login_result(self, email, password)
            if login_error_is_true[0] is True:
                self.logger.info("login email is null msg : %s" % login_error_is_true[1])
                return login_error_is_true[1]
            else:
                self.logger.info("login email is null msg : %s" % login_error_is_true[1])
                self.elt.get_screenshot()
                return login_error_is_true[1]

        except Exception as e:
            return e

    def test_password_null(self):
        #密码为空
        try:
            email = self.login_msg.return_login_email()[0]
            password = ''
            login_error_is_true = Login.return_login_result(self, email, password)
            if login_error_is_true[0] is True:
                self.logger.info("login password is null msg : %s" % login_error_is_true[1])
                return login_error_is_true[1]
            else:
                self.logger.info("login password is null msg : %s" % login_error_is_true[1])
                self.elt.get_screenshot()
                return login_error_is_true[1]

        except Exception as e:
            return e

    def test_login_regsiter(self):
        #登录相等于系统自动注册
        try:
            email = self.login_msg.rd_email()
            #保存到login_email
            read_login_email = self.date.read_doc(self.path)
            self.date.save_doc(self.path,read_login_email.replace(read_login_email,email))

            password = self.login_msg.return_password()
            login_register_is_true = Login.return_login_result(self, email, password)
            if login_register_is_true[0] is True:
                self.logger.info("login is register msg : %s" % login_register_is_true[1])
                return login_register_is_true[1]
            else:
                self.logger.info("login is register  msg : %s" % login_register_is_true[1])
                self.elt.get_screenshot()
                return login_register_is_true[1]


        except Exception as e:
            return e


    def return_login_result(self,email,password):
        #邮箱
        self.elt.input_send("id","login-email",email)
        #密码
        self.elt.input_send("id", "login-password", password)
        #点击Login
        self.elt.click("id","login-submit")
        time.sleep(5)
        login_success = self.elt.common("id","__nuxt").is_displayed()
        print(login_success)
        if login_success:
            login_text = self.elt.get_text("xpath", "//*[@id='__layout']/div/div/div/div/div[2]/div/p")
            print(login_text)
            if "Welcome," in login_text:
                return True, "login success"
            else:
                return False, "login fail"
        else:
            pass
            login_error_msg = self.elt.get_text("xpath","//*[@id='customer_login']/div[3]/p")
            if login_error_msg == "Please enter a valid email address":
                return  True , "email null verification success"
            elif login_error_msg == "":
                password_error_msg = self.elt.get_text("xpath","//*[@id='customer_login']/div[4]/p")
                if password_error_msg == "Please enter a password that is at least 6 characters long and includes a number":
                    return  True , "password null verification success"
                else:
                    return  False ,"password null verification fail"
            else:
                return  False ,"no such elements"




    def test_login_fail(self,email,password):
        #登录失败
        try:
            # 邮箱
            self.elt.input_send("id", "login-email", email)
            # 密码
            self.elt.input_send("id", "login-password", password)
            # 点击Login
            self.elt.click("id", "login-submit")
            time.sleep(5)
            login_msg = self.elt.common("xpath", "//*[@id='tt-pageContent']/div[1]").get_attribute("class")
            # print(login_msg)
            if login_msg == "user-secsern":
                login_text = self.elt.get_text("xpath", "//*[@id='tt-pageContent']/div[1]/div[1]/div")
                # print(login_text)
                if "Welcome," in login_text:
                    return True, "login success"
                else:
                    return False, "login fail"
            elif login_msg == "container-indent login-indent":
                login_error_msg = self.elt.get_text("xpath", '//*[@id="customer_login"]/div[1]/div/ul/li')
                # print(login_error_msg)
                time.sleep(1)
                if login_error_msg == "Incorrect email or password.":
                    return "login error success"

                else:
                    return  "login error fail"
        except Exception as e:
            return e

