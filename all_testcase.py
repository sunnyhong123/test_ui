# coding:utf-8
import unittest,time
import HTMLTestRunner
import os

# 用例路径
os_path = os.path.dirname(__file__)
case_path = os.path.join(os_path, "test_case")

# 报告存放路径
os_report = os.path.dirname(__file__)

report_path = os.path.join(os_report, "report")

def all_case():
    try:
        discover = unittest.defaultTestLoader.discover(case_path,
                                                        pattern="test_*.py",
                                                        top_level_dir=None)
        return discover
    except Exception as ec:
        print(ec)

if __name__ == "__main__":
    try:
        # 1、获取当前时间，这样便于下面的使用。
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 2、html报告文件路径
        report_abspath = os.path.join(report_path, "result_" + now + ".html")
        # 3、打开一个文件，将result写入此file中
        fp = open(report_abspath, "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u'Mpow官网自动化测试报告,测试结果如下：',
                                               description=u'用例执行情况：')
                                               # verbosity=2)
        # 4、调用add_case函数返回值
        runner.run(all_case())
        fp.close()
    except Exception as e:
        print(e)
