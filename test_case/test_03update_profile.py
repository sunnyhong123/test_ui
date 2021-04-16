#coding=utf-8
import unittest
from selenium import webdriver
from modular import register,account
from public import login_system,obtain_email,rd_email_name
from selenium.common.exceptions import TimeoutException
from datetime import datetime

from modular import login

class Register(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        # options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=options)

        cls.driver = webdriver.Chrome()
        cls.url = "https://www.xmpow.com/account/register?preview_theme_id=81714741366"
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.register = register.Register(cls.driver)
        cls.rd_all = rd_email_name.RD(cls.driver)
        cls.obtain = obtain_email.ObtainEmail(cls.driver)
        cls.act = account.MyAccount(cls.driver)

        cls.login = login.Login(cls.driver)

    def test_01register_success(self):
        '''验证输入随机邮箱和密码注册成功'''
        try:
            self.driver.get(self.url)
        except TimeoutException:
            print("Time out")
        email = self.rd_all.rd_email()
        register_result =self.register.return_register_result(email,"123456")[1]
        self.assertEqual("register success",register_result)

    # def test_01login_success(self):
    #     '''断言邮箱密码正确登录成功'''
    #     self.driver.get(self.url)
    #     login_result = self.login.test_login()
    #     self.assertEqual("login success", login_result)


    def test_02submit_msg(self):
        '''断言submit个人信息是否成功'''
        submit_msg_result = self.act.my_account()
        self.assertEqual("submit success",submit_msg_result)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
