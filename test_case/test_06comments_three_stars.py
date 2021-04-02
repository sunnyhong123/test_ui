#coding=utf-8
import unittest
from selenium import webdriver
from modular.register_warranty import WarrantyAct
from public import login_system
from public.rd_email_name import RD
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
        cls.rd = RD(cls.driver)
        cls.date = GetDate(cls.driver)
        cls.w_path = "\\databases\\warranty_email.txt"
        cls.account = cls.rd.rd_email()

    def test_01register_warranty(self):
        """验证注册延保流程是否成功"""
        self.driver.get(self.url)
        result = self.rw.register_warranty(self.account,"702-4500754-8597066")
        self.assertEqual("register success",result)

    def test_02comments_stars_3(self):
        """验证评3星流程是否正常"""
        result = self.rw.input_three_start()
        self.assertEqual("input three start success",result)


    def test_03delete_email(self):
        """调接口删除账号"""
        result = delete_email("1",self.account)
        self.assertEqual("delete email success",result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()