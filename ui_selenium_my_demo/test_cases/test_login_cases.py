import unittest

from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.common.by import By

from page_object.login_page import LoginPage

@ddt
class Cases(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/data.yaml')
    def test_01(self,**kwargs):
        self.driver.delete_all_cookies()
        self.lp.login(kwargs['user'],kwargs['pwd'])

        if not kwargs['user'] or not kwargs['pwd']:
            alert = self.driver.switch_to.alert
            self.assertIn(kwargs['msg'],alert.text)
            alert.accept()
        else:
            loc = (By.XPATH, '//p[text()="{}"]'.format(kwargs['msg']))
            p = self.lp.locator(loc)
            self.assertEqual(p.text, kwargs['msg'])

# if __name__ == '__main__':
#     unittest.main()