#coding=utf-8
import unittest
from selenium import webdriver
from modular.subscribe import Subscirbe

class Subscript(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.url = "https://www.xmpow.com/?preview_theme_id=81714741366"
        cls.sb = Subscirbe(cls.driver)
        cls.driver.get(cls.url)


    def test_1subcript(self):
        """验证订阅页面是否正常"""
        result = self.sb.subscribe_success()
        self.assertEqual("subscribe success",result)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



if __name__ == '__main__':
    unittest.main()
