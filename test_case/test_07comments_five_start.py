#coding=utf-8
import unittest
from selenium import webdriver
from modular.register_warranty import WarrantyAct
from public import login_system
from public.rd_email_name import RD
from public.readxlsx import GetDate
from public.interface_login import delete_email

from selenium.webdriver.support.wait import WebDriverWait


class Warranty(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # WebDriverWait(cls.driver,20,0.5).until(lambda el: cls.driver.find_element_by_xpath("//[@id='a']/h3/a") )
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
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
        result = self.rw.register_warranty(self.account,"112-7156551-7110637")
        self.assertEqual("register success",result)

    def test_02comments_stars_5(self):
        """验证评5星流程是否正常"""
        result = self.rw.input_five_start()
        self.assertEqual("warranty and submit rv success",result)


    def test_03delete_email(self):
        """调接口删除账号"""
        result = delete_email("1",self.account)
        self.assertEqual("delete email success",result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()