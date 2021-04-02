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
        # cls.url = "https://www.xmpow.com/pages/warranty?preview_theme_id=81714741366"
        cls.url = "https://www.xmpow.com/pages/warranty?preview_theme_id=81714741366"
        cls.system_url = "https://brandwtest.patozon.net/#/login?redirect=%2Fdashboard"
        cls.rw = WarrantyAct(cls.driver)
        cls.sys = login_system.LoginSystem(cls.driver)
        cls.rd = RD(cls.driver)
        cls.date = GetDate(cls.driver)
        cls.w_path = "\\databases\\warranty_email.txt"

    def test_01register_warranty(self):
        """验证注册延保流程是否成功"""
        self.driver.get(self.url)
        # 账号
        account = self.rd.rd_email()
        w_email = self.date.read_doc(self.w_path)
        self.date.save_doc(self.w_path, w_email.replace(w_email, account))
        reuslt = self.rw.register_warranty(account,"113-3646966-9642628")
        self.assertEqual("register success",reuslt)

    def test_02delete_email(self):
        """调接口删除账号"""
        email = self.date.read_doc(self.w_path)
        result = delete_email("1",email)
        self.assertEqual("delete email success",result)

    # def test_02delete_email(self):
    #     '''验证会员系统删除测试账号是否成功'''a
    #     self.driver.get(self.system_url)
    #     delete_email_result = self.sys.Choice_system("mpow", "3")
    #     self.assertEqual("delete email success", delete_email_result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

