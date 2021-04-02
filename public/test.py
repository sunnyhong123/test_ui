#coding=utf-8

# import re,json,xlrd
# import random
# import time
# import os
# from datetime import datetime
# # for i in range(5):
# #     register_testMail = ''.join(random.sample('123456789abcdefghijklmnopqrstuvwxyzABCDEF._', 8)) + "@chacuo.net"
# #     print(register_testMail)
# #
# #
# # for i in range(5):
# #     register_testUsername = ''.join(random.sample('abcdefghijklmnABCDEFG ._', 5))
# #     print(register_testUsername)
#
# # now = time.strftime("%Y-%m-%d", time.localtime())
#
# now = datetime.now().strftime("%Y-%m-%d")
# print(now)
#
# # os_path = os.path.split(os.path.dirname(__file__))[0]
# # print(os_path)
# os_path = os.path.dirname(__file__)
# # os_path = os.path.split(os.path.dirname(__file__))[0]
# print(os_path)
#

# f = open(r"C:\Users\Administrator\Desktop\1.txt","r",encoding="utf-8")
# r = f.readlines()
# print(r)
# f.close()    [TimingData]

# with open(r"C:\Users\Administrator\Desktop\1.txt","r",encoding="utf-8") as f:
#     data = f.read()
#     print(data)
    # for line in data:
    #     result = re.match("",line)
    # list_1 = re.findall(r"([a-z+]:)","[TimingData]")
    # print(list_1)

# date_list = []
# get_file = xlrd.open_workbook(r"C:\Users\Administrator\Desktop\1.xlsx")
# get_sheet = get_file.sheet_by_name(1)
# get_rows = get_sheet.nrows
# print(get_rows)
# for i in range(get_rows):
#     if i > 0:
#         date_list.append(get_sheet.row_values(i))
#      print(date_list)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium .webdriver.support import expected_conditions as EC
#
# # options = webdriver.ChromeOptions()
# # options.add_argument("headless")
# # driver = webdriver.Chrome(chrome_options=options)
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://www.xmpow.com/account/register?preview_theme_id=81714741366")
# # driver.get_screenshot_as_file(
# #     r"F:\Mpow_test\error_captcha\%s.png" )
# timeout = WebDriverWait(driver,10)
# timeout.until(EC.element_to_be_clickable((By.ID ,"register-submit"))).click()

# i = 0
# while i < 9:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         print(f"{j}*{i}={i*j } ",end="")
#     print()

# #100以内所有质数
# i = 2
# while i <= 100:
#     flag = True
#     j = 2
#     while j < i:
#         if i % j == 0:
#             flag = False
#         j += 1
#     if flag:
#         print(i)
#     i+=1

# sum = lambda a,b: a*b
# print(sum(2,3))

"""
abc 转化为 a,b,c
"""
# lists = "abc"
# codes = []
# for i in lists:
#     codes.append(i)
# print(codes)

#列表推导式
# lists = "abc"
# codes = [i for i in lists]
# print(codes)

# colors = ["black","white"]
# sizes = ["S","M","L"]
# for i in colors:
#     for n in sizes:
#         print(i,n)
# #
# values = [(i,n)for i in colors for n in sizes]
# print(values)


import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")



