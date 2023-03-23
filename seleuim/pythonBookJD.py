# 导入seleninum webdriver接口
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

broswer=webdriver.Firefox()
broswer.get('https://www.jd.com/')
broswer.find_element(By.XPATH, '//*[@id="key"]').send_keys("python书籍")
# print("1")

broswer.find_element(By.XPATH, "//*[@class='form']/button").click()
print("1")
#阻塞3秒
# broswer.implicitly_wait(10)
# 自动退出浏览器
# broswer.quit()