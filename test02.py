"""
@Filename:  /test02
@Author:   lianpengwei
@Time:    2022/9/21 17:40
@Describe:  ...
"""
from webdriver_helper import get_webdriver

driver = get_webdriver()

driver.get('http://127.0.0.1/Home/user/login.html')

driver.find_element('xpath', '//*[@id="username"]').send_keys('18513')

input('enter')
driver.quit()