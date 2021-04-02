#coding=utf-8
from public import Commonlib,log,rd_email_name,readxlsx
import time
# logger = log.Mylog("Mpow").getlog()

class Register(object):
    def __init__(self,dr):
        self.driver = dr
        self.elt = Commonlib.Common(self.driver)
        self.logger = log.Mylog("Mpow").getlog()
        self.rd_all = rd_email_name.RD(self.driver)
        self.path = "\\databases\\rd_email.txt"
        self.date = readxlsx.GetDate(self.driver)

    def test_register(self):
        #正常注册
        try:
            # 邮箱
            email = self.rd_all.rd_email()
            #保存到随机邮箱
            read_rd_email = self.date.read_doc(self.path)
            self.date.save_doc(self.path, read_rd_email.replace(read_rd_email, email))
            # 密码
            # password1 = self.rd_all.return_password()
            # password2 = self.rd_all.return_password()
            password1 = "123456"

            register_is_true = Register.return_register_result(self,email,password1)
            if register_is_true[0] is True:
                self.logger.info("register result: %s"%register_is_true[1])
                return register_is_true[1]
            else:
                self.logger.error("register error: %s"%register_is_true[1])
                self.elt.get_screenshot()
                return register_is_true[1]
        except Exception as e:
            return  e

    def test_error_register(self):
        #邮箱格式错误
        try:
            # 邮箱
            email = "heidibhannagmail.com"
            # 密码
            password1 = self.rd_all.return_password()
            error_register_is_true = Register.return_register_result(self,email,password1)
            if error_register_is_true[0] is True:
                self.logger.info(u"验证错误格式注册信息注册失败：%s" %error_register_is_true[1])
                return error_register_is_true[1]
            else:
                self.logger.error(u"验证错误格式注册信息注册失败错误信息为：%s" % error_register_is_true[1])
                self.elt.get_screenshot()
                return  error_register_is_true[1]

        except Exception as e:
            return e

    def test_register_email_null(self):
        #邮箱为空
        try:
            #邮箱
            email = ""
            # 密码
            password1 = self.rd_all.return_password()
            null_register_is_true = Register.return_register_result(self,email,password1)
            if null_register_is_true[0] is True:
                self.logger.info("email is null result: %s" %null_register_is_true[1])
                return  null_register_is_true[1]
            else:
                self.logger.error("email is null error : %s" %null_register_is_true[1])
                self.elt.get_screenshot()
        except Exception as e:
            return e

    def test_register_password_null(self):
        #密码为空
        try:
            # 邮箱
            email = self.rd_all.rd_email()
            # 密码
            password1 = ''
            password_is_null_true = Register.return_register_result(self,email,password1)
            if password_is_null_true[0] is True:
                self.logger.info("password is null result: %s" %password_is_null_true[1])
                return  password_is_null_true[1]
            else:
                self.logger.error("password is null error : %s" %password_is_null_true[1])
                self.elt.get_screenshot()
        except Exception as e:
            return e

    def test_register_password_short(self):
        #密码过短
        try:
            # 邮箱
            email = self.rd_all.rd_email()
            # 密码
            password1 = self.rd_all.return_short_password()
            register_is_true = Register.return_register_result(self,email,password1)
            if register_is_true[0] is True:
                self.logger.info("register password short msg: %s"%register_is_true[1])
                # self.logger.info("register result: %s"%register_is_true[1])
                return register_is_true[1]
            else:
                self.logger.error("register password short msg: %s"%register_is_true[1])
                # self.logger.error("register error: %s"%register_is_true[1])
                self.elt.get_screenshot()
                return register_is_true[1]

        except Exception as e:
            return  e

    def test_register_password_different(self):
        #输入不相同的密码
        try:
            # 邮箱
            email = self.rd_all.rd_email()
            # 密码
            password1 = self.rd_all.return_password()
            register_is_true = Register.return_register_result(self,email,password1)
            if register_is_true[0] is True:
                self.logger.info("register password different result: %s"%register_is_true[1])
                # self.logger.info("register result: %s"%register_is_true[1])
                return register_is_true[1]
            else:
                self.logger.error("register password different result : %s"%register_is_true[1])
                # self.logger.error("register error: %s"%register_is_true[1])
                self.elt.get_screenshot()
                return register_is_true[1]
        except Exception as e:
            return e


    def return_register_result(self,email,password1):
        try:
            #用户名 first last
            name = self.rd_all.rd_name()
            first_name = name.split(" ")[0]
            # print(first_name)
            last_name = name.split(" ")[1]
            # print(last_name)
            self.elt.input_send("id","register-firstname",first_name)
            self.elt.input_send("id", "register-lastname", last_name)

            self.elt.input_send("id", "register-email", email)

            self.elt.input_send("id", "register-password", password1)

            #点击Create Account //*[@id="register-submit"]
            self.elt.click("id","register-submit")
            time.sleep(8)
            self.elt.get_screenshot()
            login_msg = self.elt.common("xpath","//*[@id='tt-pageContent']/div[1]").get_attribute("class")

            if  login_msg == "":
                login_text = self.elt.get_text("xpath","//*[@id='__layout']/div/div/div/div/div[2]/div/p")
                print(login_text)
                if "Welcome," in login_text:
                    #保存注册成功邮箱
                    return True ,"register success"
                else:
                    return  False , "register fail"
            elif login_msg == "container-indent register-indent":
                time.sleep(2) #//*[@id="create_customer"]/div[4]/p    //*[@id="create_customer"]/div[5]/p
                email_error_msg = self.elt.get_text("xpath","//*[@id='customer_login']/div[5]/p")
                if email_error_msg == "Please enter a valid email address":
                    return  True , "error verification success"
                elif email_error_msg == "":                         #//*[@id="create_customer"]/div[5]/p/text()//*[@id="create_customer"]/div[5]/p
                    password_error_msg = self.elt.get_text("xpath","//*[@id='customer_login']/div[6]/p")
                    if password_error_msg == "Please enter a password that is at least 6 characters long":
                        return  True , "password verification success"
                    elif password_error_msg == "Please ensure that both passwords match":
                        return  True , "password different verification success"
                    else:
                        return  False , "password verification fail"
                else:
                    return  False , "error register fail"

            else:
                return False ,"not such elements"
        except Exception as e:
            return  e
