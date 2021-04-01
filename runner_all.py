import unittest
import time
from BeautifulReport import BeautifulReport

# 获取时间戳（当前时间）
current_time = time.strftime('%Y-%m-%d-%H-%M-%S')
# 组织报告文件名字
file_name = current_time + '-report.html'

if __name__=="__main__":
    # 抓取测试用例的名字
    cases = unittest.defaultTestLoader.discover('./test_case')
    runner = BeautifulReport(cases)     # 实例化BR
    runner.report('VT接口自动化测试', file_name, './report')  # 对象调用类中的方法

