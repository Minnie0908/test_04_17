


# 入口文件
# 处理报告
# 引入HTMLTestRunner模块
from config.HTMLTestRunner import HTMLTestRunner
from base.utils import get_report_name
import unittest


# 主程序执行（固定写法）
if __name__ == '__main__':
    # 说明：HTMLTestRunner生成的报告是.html文件
    with open('reports/{}.html'.format(get_report_name('ceniu')), 'wb') as f:
        discover = unittest.defaultTestLoader.discover(start_dir='./test_cases', pattern='test_*.py')  # 注意必须执行单元测试框架的代码
        runner = HTMLTestRunner(stream=f, title='测试标题', description='描述本次报告的整体内容')
        runner.run(discover)






