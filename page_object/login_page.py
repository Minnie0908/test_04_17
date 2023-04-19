# 登录页面对象
# 作用：实现自动登录
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # 1.组件定位
    url = 'http://43.226.74.244/ecshop/user.php'
    user = (By.NAME, 'username')
    pwd = (By.NAME, 'password')
    btn = (By.XPATH, '//input[@name="submit"]')

    # 2.操作流程
    def login(self, u, p):
        # 1.打开页面
        self.open(self.url)     # open方法是继承过来的，而self.url获取当前类中的
        # 2.最大化
        self.max()
        # 3.隐式等待
        self.wait(15)
        # 4.输入账号
        self.input(self.user, u)
        # 5.输入密码
        self.input(self.pwd, p)
        # 6.等待1秒
        self.sleep(1)
        # 7.点击登录按钮
        self.click(self.btn)
        # 8.等到1秒
        self.sleep(1)

# 代码测试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)    # 需要传递driver对象，因为继承了BasePage
    lp.login('chen123', 'chen123')


