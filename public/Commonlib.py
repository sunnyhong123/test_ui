#coding=utf-8
from selenium.webdriver.support.ui import Select
import random,time
import datetime,os


class Common(object):
    def __init__(self,dr):
        self.driver = dr

    def common(self,type,value):
        if type == "xpath":
            return self.driver.find_element_by_xpath(value)

        elif type =="elements":
            return self.driver.find_elements_by_xpath(value)

        elif type == "id":
            return self.driver.find_element_by_id(value)

        elif type == "name":
            return self.driver.find_element_by_name(value)

        elif type == "link":
            return self.driver.find_element_by_link_text(value)

        elif type == "css":
            return self.driver.find_element_by_selector(value)

        elif type == "class_name":
            return self.driver.find_element_by_class_name(value)

    def input_send(self, type, value, data):
        try:
            if type == "id":
                el = self.driver.find_element_by_id(value)
                el.clear()
                return el.send_keys(data)
            elif type == "name":
                el = self.driver.find_element_by_name(value)
                el.clear()
                return el.send_keys(data)
            elif type == "class_name":
                el = self.driver.find_element_by_class_name(value)
                el.clear()
                return el.send_keys(data)
            elif type == "xpath":
                el = self.driver.find_element_by_xpath(value)
                el.clear()
                return el.send_keys(data)
            elif type == "css":
                el = self.driver.find_element_by_css_selector(value)
                el.clear()
                return el.send_keys(data)
            elif type == "link":
                el = self.driver.find_element_by_link_text(value)
                el.clear()
                return el.send_keys(data)
            elif type == "part":
                el = self.driver.find_element_by_partial(value)
                el.clear()
                return el.send_keys(data)
            elif type == "tag":
                el = self.driver.find_element_by_tag(value)
                el.clear()
                return el.send_keys(data)
            else:
                print("没有发现元素...")

        except Exception as e:
            raise Exception(e)

    def click(self, type, value):
        # 点击操作
        try:
            if type == "id":
                el = self.driver.find_element_by_id(value)
                return el.click()
            elif type == "name":
                el = self.driver.find_element_by_name(value)
                return el.click()
            elif type == "class_name":
                el = self.driver.find_element_by_class_name(value)
                return el.click()
            elif type == "xpath":
                el = self.driver.find_element_by_xpath(value)
                return el.click()
            elif type == "css":
                el = self.driver.find_element_by_css_selector(value)
                return el.click()
            elif type == "link":
                el = self.driver.find_element_by_link_text(value)
                return el.click()
            elif type == "part":
                el = self.driver.find_element_by_partial(value)
                return el.click()
            elif type == "tag":
                el = self.driver.find_element_by_tag(value)
                return el.click()
            else:
                print("没有发现元素...")

        except Exception as e:
            raise Exception(e)

    def get_text(self, type, value):
        # 获取文本值
        try:
            if type == "id":
                el = self.driver.find_element_by_id(value)
                return el.text
            elif type == "name":
                el = self.driver.find_element_by_name(value)
                return el.text
            elif type == "class_name":
                el = self.driver.find_element_by_class_name(value)
                return el.text
            elif type == "xpath":
                el = self.driver.find_element_by_xpath(value)
                return el.text
            elif type == "css":
                el = self.driver.find_element_by_css_selector(value)
                return el.text
            elif type == "link":
                el = self.driver.find_element_by_link_text(value)
                return el.text
            elif type == "part":
                el = self.driver.find_element_by_partial(value)
                return el.text
            elif type == "tag":
                el = self.driver.find_element_by_tag(value)
                return el.text
            else:
                print("没有发现元素...")

        except Exception as e:
            return e

    def clear(self, type, value):
        # 清除数据
        try:
            if type == "id":
                el = self.driver.find_element_by_id(value)
                return el.clear()
            elif type == "name":
                el = self.driver.find_element_by_name(value)
                return el.clear()
            elif type == "class_name":
                el = self.driver.find_element_by_class_name(value)
                return el.clear()
            elif type == "xpath":
                el = self.driver.find_element_by_xpath(value)
                return el.clear()
            elif type == "css":
                el = self.driver.find_element_by_css_selector(value)
                return el.clear()
            elif type == "link":
                el = self.driver.find_element_by_link_text(value)
                return el.clear()
            elif type == "part":
                el = self.driver.find_element_by_partial(value)
                return el.clear()
            elif type == "tag":
                el = self.driver.find_element_by_tag(value)
                return el.clear()
            else:
                print("没有发现元素...")

        except Exception as e:
            return e

    def switch_to(self):
        #切入框架
        try:
            #self.driver.switch_to_default_content()
            self.driver.switch_to_default_content()
            self.driver.switch_to.frame(1)
            #
            # self.driver.switch_to_frame(self.driver.find_element_by_xpath(
            #     "html/body/div[1]/div[1]/div[1]/div[2]/iframe").find_element_by_id('tab_frame_2'))
            # print("切入框架成功...")
            # self.driver.switch_to_frame(
            #     self.Elt.element_by_xpath("html/body/div[1]/div[1]/div[1]/div[2]/iframe").find_element_by_id("tab_frame_2"))
        except Exception as e :
            return e

    def random_select(self,code):
        #下拉框操作
        try:
            get_select_option = self.driver.find_elements_by_xpath("//select[@id='%s']/option" % code)
            select_list = []
            for option in get_select_option:
                if option.get_attribute("value") != "":
                    select_list.append(option.get_attribute("value"))
            rd_select = select_list[random.randrange(0, len(select_list))]
            sd = self.driver.find_element_by_xpath("//select[@id='%s']" % code)
            Select(sd).select_by_value(rd_select)
        except Exception as e:
            return e

    def js_execute(self,num):
        #下拉滚动操作
        try:
            js = "window.scrollTo(0,%d)"% num
            self.driver.execute_script(js)
            time.sleep(1)
        except Exception as e :
            return e

    def input_datetime(self):
        #创建项目获取  计划开始日期   计划结束日期
        try:
            first_td_time = datetime.datetime.now()
            get_oem_tr = self.driver.find_elements_by_xpath("//div[@id='tab_OEM']/table/tbody/tr")
            len_num = len(get_oem_tr) - 1
            for num in range(len_num):
                if num == 0:
                    tr_num = "%d" % int(num)
                elif num < 19:
                    tr_num = "%d" % int(num + 1)

                    if tr_num == "7":
                        tr_num = str(int(tr_num)+2)

                    elif tr_num == "13":
                        tr_num = "%d" % int(int(tr_num) + 1)

                delta = datetime.timedelta(days=num + 1)
                second_td_time = first_td_time + delta
                # 取消readonly设置
                # start_js = "document.getElementsByName('OEM-planCompletionDate-%s')[0].readOnly = false" % tr_num
                # self.driver.execute_script(start_js)
                # self.driver.find_element_by_name("OEM1-planStartDate-%s" % tr_num).clear()
                # self.driver.find_element_by_name("OEM1-planStartDate-%s" % tr_num).send_keys(
                #     second_td_time.strftime("%Y-%m-%d"))
                complete_js = "document.getElementsByName('OEM-planCompletionDate-%s')[0].readOnly = false" % tr_num
                self.driver.execute_script(complete_js)
                self.driver.find_element_by_name("OEM-planCompletionDate-%s" % tr_num).clear()
                self.driver.find_element_by_name("OEM-planCompletionDate-%s" % tr_num).send_keys(
                    second_td_time.strftime("%Y-%m-%d"))
        except Exception as e:
            return e

    def select_type(self, type, value, num, data):
        # 下拉框定位
        try:
            msg_select = self.common(type, value)
            if num == "1":
                Select(msg_select).select_by_index(data)
            elif num == "2":
                Select(msg_select).select_by_value(data)
            elif num == "3":
                Select(msg_select).select_by_visible_text(data)
            else:
                print("定位下拉框没有找到元素...")
        except Exception as e:
            return e

    def num_rad(self):
        num = random.randrange(1,1000)
        return  num

    def search_sku(self,value,data):
        #查询sku
        try:
            first_text =self.get_text("xpath","//table[@id='listTable']/tbody/tr/td[1]")
            if len(first_text) >0:
                self.input_send("id",value,data)
                self.click("id","searchBtn")
                time.sleep(1)
                second_text =self.common("elements","//table[@id='listTable']/tbody/tr")
                if len(second_text) >0:
                    return "search success"
                else:
                    return  "search fail"
            else:
                print("首单列表为空...")
        except Exception as e :
            return e

    def get_screenshot(self):
        try:
            self.driver.get_screenshot_as_file(r"F:\Mpow_test\error_captcha\%s.png"%datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
        except Exception as e:
            return  e

    def sort(self):
        try:
            #获取升降序
            get_order_type = self.driver.find_element_by_xpath("//*[@id='listTable']/thead/tr/th[2]")\
                .get_attribute("data-orderdirection")
            get_frist_id = self.driver.find_element_by_xpath("//*[@id='listTable']/tbody/tr[1]/td[2]").text
            get_tr = self.driver.find_elements_by_xpath("//*[@id='listTable']/tbody/tr/td[2]")
            array_list = []
            if len(get_tr) != 0:
                for tr in get_tr:
                    array_list.append(tr.text)
                if get_order_type == "asc":
                    min_text = min(array_list)
                    if get_frist_id == min_text:
                        return True ,"sort success"
                elif get_order_type == "desc":
                    max_text = max(array_list)
                    if get_frist_id == max_text:
                        return  True,"sort success"
                else:
                    return  False,"sort fail"
            else:
                return False,"sort date is null"

        except Exception as e:
            self.get_screenshot()

            return e

    def quit_role(self):
        try:
            #退出框架
            self.driver.switch_to_default_content()
            #点击用户
            self.click("id","loginUserName")
            time.sleep(0.5)
            self.click("id","user-quit")
        except Exception as e:
            return e

    def edit_or_view_is_start(self, div_id):
        #获取页面元素class 判断点击操作是否完成（等待页面加载完成再进行下一步操作）
        try:
            is_false = False
            num = 0
            while is_false is False:
                if num >= 60:
                    raise Exception("edit or view fail timeout 30 second!")
                class_status = self.driver.find_element_by_id(div_id).get_attribute("class")
                time.sleep(0.5)
                if "in" in class_status:
                    is_false = True
                else:
                    num += 1
        except Exception as e:
            raise Exception(e)
