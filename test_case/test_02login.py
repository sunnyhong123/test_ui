#coding=utf-8
import unittest
from selenium import webdriver
from modular import login
from public import log,login_system

class Login(unittest.TestCase):
    def setUp(self):
        # options = webdriver.ChromeOptions()
        # #使用无界面浏览器执行代码
        # options.add_argument("headless")
        # #关闭浏览器提示信息
        # options.add_argument("disable-infobars")
        # self.driver = webdriver.Chrome(chrome_options=options)

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()   #self.url = "https://www.xmpow.com/account/login?preview_theme_id=81126555766"
        self.url = "https://www.xmpow.com/account/login?preview_theme_id=81714741366"
        self.system_url = "https://testbrand.patozon.net/#/login?redirect=%2Fdashboard"
        self.sys = login_system.LoginSystem(self.driver)
        self.driver.get(self.url)
        # class_status = self.driver.find_element_by_id("Modalnewsletter").get_attribute("class")
        # if class_status == "modal fade show":
        #     self.driver.find_element_by_xpath('//*[@id="Modalnewsletter"]/div/div/div[1]/button').click()
        self.logger = log.Mylog("Mpow").getlog()
        self.login = login.Login(self.driver)

    def test_01login_success(self):
        '''断言邮箱密码正确登录成功'''
        try:
            login_result = self.login.test_login()
            self.assertEqual("login success",login_result)
        except Exception as e:
            self.logger.error("login exception msg : %s" % e)

    # def test_02username_null(self):
    #     '''断言邮箱为空登录失败'''
    #     email_null_result = self.login.test_email_null()
    #     self.assertEqual("email null verification success", email_null_result)
    #
    # def test_03password_null(self):
    #     '''断言密码为空登录失败'''
    #     password_null_resutl = self.login.test_password_null()
    #     self.assertEqual("password null verification success",password_null_resutl)
    #
    # def test_04login_fail_username(self):
    #     '''断言用户名错误,密码正确登录失败'''
    #     login_result = self.login.test_login_fail("sunny@patazon.net","123456")
    #     self.assertEqual("login error success",login_result)
    #
    # def test_05login_fail_password(self):
    #     '''断言用户名正确,密码错误登录失败'''
    #     login_result = self.login.test_login_fail("Sunny_hong@patazon.net","123456456789")
    #     self.assertEqual("login error success",login_result)
    #


    # def test_04login_register(self):
    #     '''断言登录输入任何邮箱和密码系统自动注册成功'''
    #     login_register_result = self.login.test_login_regsiter()
    #     self.assertEqual("login success",login_register_result)

    # def test_05delete_email(self):
    #     '''验证会员系统删除测试账号是否成功'''
    #     self.driver.get(self.system_url)
    #     delete_email_result = self.sys.Choice_system("mpow", "1")
    #     self.assertEqual("delete email success", delete_email_result)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

