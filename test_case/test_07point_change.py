# coding=utf-8
import unittest
from selenium import webdriver

class Login(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.register_url =  "https://www.xmpow.com/pages/points-store?preview_theme_id=81126555766"

    def test_01register_success(self):
        '''注册是否成功'''
        # self.driver.get("http://24mail.chacuo.net/enus")
        # self.get_24email.obtainemail()
        pass

    def test_02get_point(self):
        '''获取积分是否正常'''
        pass

    # def test_03change_product(self):
    #     '''兑换实物是否成功'''
    #     pass
    #
    # def test_04change_gift_card(self):
    #     '''兑换折扣码是否成功'''
    #     pass
    #
    # def test_05change_coupons(self):
    #     '''兑换优惠券是否成功'''
    #     pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()