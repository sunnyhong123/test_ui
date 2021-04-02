#coding=utf-8
import unittest
from selenium import webdriver
from modular import register
from public import login_system,obtain_email
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from datetime import datetime


class Register(unittest.TestCase):
    def setUp(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        # self.driver = webdriver.Chrome(chrome_options=options)

        self.driver = webdriver.Chrome()
        self.url = "https://www.xmpow.com/account/register?preview_theme_id=81714741366"
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.register = register.Register(self.driver)
        self.obtain = obtain_email.ObtainEmail(self.driver)
        # self.sys = login_system.LoginSystem(self.driver)

    def test_01register_success(self):
        '''验证输入随机邮箱和密码注册成功'''
        try:
            self.driver.get(self.url)
        except TimeoutException:
            print("Time out")
        register_result =self.register.test_register()
        self.assertEqual("register success",register_result)


    def test_03register_error(self):
        '''验证输入错误格式邮箱注册失败'''
        self.driver.get(self.url)
        register_error_result = self.register.test_error_register()
        self.assertEqual("error verification success",register_error_result)

    def test_04register_null(self):
        '''验证邮箱为空注册失败'''
        self.driver.get(self.url)
        register_null_result = self.register.test_register_email_null()
        self.assertEqual("error verification success",register_null_result)

    def test_05register_password_null(self):
        '''验证密码为空注册失败'''
        self.driver.get(self.url)
        register_password_null_result = self.register.test_register_password_null()
        self.assertEqual("password different verification success",register_password_null_result)

    def test_06register_password_short(self):
        '''验证输入密码过短注册失败'''
        self.driver.get(self.url)
        register_password_short_resutl = self.register.test_register_password_short()
        self.assertEqual("password verification success",register_password_short_resutl)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

