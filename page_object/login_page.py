from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):

    url = 'http://192.168.10.250/ecshop/user.php'
    user = (By.NAME,'username')
    pwd = (By.NAME,'password')
    btn = (By.XPATH,'//input[@name="submit"]')

    def login(self,u,p):

        self.open(self.url)

        self.max()

        self.wait(15)

        self.input(self.user,u)

        self.input(self.pwd,p)

        self.click(self.btn)

        # self.sleep()
        # self.quit()


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     lp = LoginPage(driver)
#     lp.login('test','123456')
