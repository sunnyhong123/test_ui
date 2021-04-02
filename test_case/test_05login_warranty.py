#coding=utf-8
import unittest
from selenium import webdriver
from modular.register_warranty import WarrantyAct
from public import login_system
from public.readxlsx import GetDate
from public.interface_login import delete_email

class Warranty(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()   #https://www.xmpow.com/?preview_theme_id=81714741366
        cls.url = "https://www.xmpow.com/pages/warranty?preview_theme_id=81714741366"
        cls.system_url = "https://brandwtest.patozon.net/#/login?redirect=%2Fdashboard"
        cls.rw = WarrantyAct(cls.driver)
        cls.sys = login_system.LoginSystem(cls.driver)
        cls.date = GetDate(cls.driver)
        cls.r_e_path = "\\databases\\rd_email.txt"

    def test_01login_warranty(self):
        """断言登录延保是否成功"""
        self.driver.get(self.url)
        # 邮箱
        email = self.date.read_doc("\\databases\\rd_email.txt")
        reuslt = self.rw.login_warranty(email,"111-2299836-2462612")
        self.assertIn("login warranty success", reuslt)

    def test_02delete_email(self):
        """调接口删除账号"""
        email = self.date.read_doc(self.r_e_path)
        result = delete_email("1", email)
        self.assertEqual("delete email success", result)

    # def test_02delete_email(self):
    #     '''验证会员系统删除测试账号是否成功'''
    #     self.driver.get(self.system_url)
    #     delete_email_result = self.sys.Choice_system("mpow", "2")
    #     self.assertEqual("delete email success", delete_email_result)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

