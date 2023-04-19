

# 封装常用功能
# 例如：访问url、最大化、元素定位、元素操作（输入、点击）、退出、关闭、设置等待、页面跳转...

import time
from base.utils import get_log

class BasePage:     # 类名建议使用大驼峰式写法
    # 日志对象
    log = get_log()

    # 1.构造方法：用于接收driver对象
    def __init__(self, driver):
        # 日志记录
        self.log.info('初始化driver对象：{}'.format(driver))
        self.driver = driver

    # 2.访问
    def open(self, url):
        self.log.info('访问{}地址'.format(url))
        self.driver.get(url=url)

    # 3.最大化
    def max(self):
        self.log.info('窗口最大化')
        self.driver.maximize_window()

    # 4.隐式等待
    def wait(self, timer=10):
        self.log.info('设置隐式等待{}秒'.format(timer))
        self.driver.implicitly_wait(timer)

    # 5.强制等待
    def sleep(self, timer=3):
        self.log.info('设置强制等待{}秒'.format(timer))
        time.sleep(timer)

    # 6.单个元素定位 ☆
    def locator(self, loc):     # locator表示定位器，loc就是(By.ID, 'one')
        # loc是元组，加上*之后，会自动映射 ☆
        # 返回被定位的元素对象 ☆
        self.log.info('正在定位{}元素'.format(loc))
        return self.driver.find_element(*loc)   # find_element的参数是2个 ☆

    # 7.输入
    def input(self, loc, content):
        self.log.info('正在输入{}内容'.format(content))
        self.locator(loc).send_keys(content)

    # 8.点击
    def click(self, loc):
        self.log.info('正在点击{}元素'.format(loc))
        self.locator(loc).click()

    # 9.切换iframe窗口
    def switch_to_frame(self, iframe):
        self.driver.switch_to.frame(iframe)

    # 10.切换web页面：基于句柄（索引）
    def switch_to_window(self, index):
        handle_ls = self.driver.window_handles  # 获取所有页面的句柄，以列表形式返回
        self.driver.switch_to.window((handle_ls[index]))

    # 11.关闭
    def close(self):
        self.log.info('关闭当前浏览器')
        self.driver.close()

    # 12.退出
    def quit(self):
        self.log.info('程序退出')
        self.driver.quit()

    # 13.xxxxx 按照业务流进行适配封装 ☆
    # ...




