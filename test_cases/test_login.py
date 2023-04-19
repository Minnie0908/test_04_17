
# 用例类
# 基于单元测试 unittest
# 需求实现：基于Yaml的6组数据测试登录功能
# 分析：浏览器如果打开6次太麻烦，所以要实现打开一次
# 结论：单元测试框架：setUpClass打开浏览器/tearDownClass关闭浏览器

import unittest
import time

from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from page_object.login_page import LoginPage

@ddt
class Cases(unittest.TestCase):
    # 类属性
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        # 打开浏览器
        cls.driver = webdriver.Chrome()
        # 获取登录对象
        cls.lp = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 用例 ☆
    # 说明：加上数据驱动之后，该用例会自动执行6次 ☆
    # 说明：但是浏览器只打开了1次，那么如果把正例放在第一位，之后的5个反例就会报错 ☆
    @file_data('../data/data.yaml') # 加载yaml文件
    def test_01(self, **kwargs):    # 可变参数（字典）
        # 如果想让正例放前面，清空Cookie ☆
        self.driver.delete_all_cookies()
        # 实现登录
        self.lp.login(kwargs['user'], kwargs['pwd'])
        # 断言：寻找 "登录成功"（3s跳转）
        # 1.如果用户名为空或密码为空
        # kwargs['user']为空
        # kwargs['pwd']为空
        if not kwargs['user'] or not kwargs['pwd']:
            alert = self.driver.switch_to.alert # 弹窗写法（之前在笔记里发过的）
            self.assertIn(kwargs['msg'], alert.text)
            # 关闭弹窗 ☆
            alert.accept()
        # 2.都不为空
        else:
            loc = (By.XPATH, '//p[text()="{}"]'.format(kwargs['msg']))
            p = self.lp.locator(loc)
            self.assertEqual(p.text, kwargs['msg'])