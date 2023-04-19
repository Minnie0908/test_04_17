import time
# from selenium import webdriver
from base.utils import get_log

class BasePage:

    log =get_log()

    def __init__(self,driver):
        self.log.info('初始化driver对象:{}'.format(driver))
        self.driver = driver
        # self.driver = webdriver.Chrome()

    def open(self,url):
        self.log.info('访问{}地址'.format(url))
        self.driver.get(url=url)

    def max(self):
        self.log.info('窗口最大化')
        self.driver.maximize_window()

    def wait(self,timer=10):
        self.log.info('设置隐式等待{}秒'.format(timer))
        self.driver.implicitly_wait(timer)

    def sleep(self,timer=3):
        self.log.info('设置强制等待{}秒'.format(timer))
        time.sleep(timer)

    def locator(self,loc):
        self.log.info('正在定位{}元素'.format(loc))
        return self.driver.find_element(*loc)

    def input(self,loc,content):
        self.log.info('正在输入{}内容'.format(content))
        self.locator(loc).send_keys(content)

    def click(self,loc):
        self.log.info('正在点击{}元素'.format(loc))
        self.locator(loc).click()

    def switch_to_frame(self,iframe):
        self.driver.switch_to.frame(iframe)

    def switch_to_window(self,index):
        handle_ls=self.driver.window_handles
        self.driver.switch_to.window(handle_ls[index])

    def close(self):
        self.log.info('关闭当前浏览器')
        self.driver.close()

    def quit(self):
        self.log.info('程序退出')
        self.driver.quit()
