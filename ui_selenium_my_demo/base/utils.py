# 自己的工具模块 ☆
# 封装了很多我们常用的工具

import time
import random
import logging
import logging.config

# 处理名字
# 思路：时间（年月日时分秒）+随机数字
def get_report_name(n='test_report'):
    timer = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    rands = str(random.randint(10000, 99999))
    return timer+'_'+n+'_'+rands

# 日志调用
def get_log():
    logging.config.fileConfig('config/log.conf')
    logger = logging.getLogger()
    return logger



