# 导入seleninum webdriver接口
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建Chrome浏览器对象
browser = webdriver.Chrome()
#访问百度网站
browser.get('http://www.baidu.com/')
#阻塞3秒
browser.implicitly_wait(5)
# 自动退出浏览器
browser.quit()