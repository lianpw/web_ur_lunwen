"""
@Filename:  /conftest
@Author:   lianpengwei
@Time:    2022/9/19 11:48
@Describe:  全局夹具
"""
import json
from json import JSONDecodeError
from pathlib import Path

import pytest
from webdriver_helper import get_webdriver, debugger

from cores.kdt import KeyWord


@pytest.fixture()
def driver():
    driver = get_webdriver()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def login_driver():
    """返回已登录的浏览器"""
    driver = get_webdriver()
    # debugger(driver)
    driver.get('http://127.0.0.1/')
    cookies = []
    path = Path('temps/cookies/cookies.json')
    if path.exists():
        try:
            with open('temps/cookies/cookies.json', 'r', encoding='utf-8') as f:
                cookies = json.load(f)
                # print(f'{cookies=}', type(cookies))
        except JSONDecodeError:
            pass

    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

    if "安全退出" not in driver.page_source:
        kw = KeyWord(driver)
        kw.key_get_url('http://127.0.0.1/Home/user/login.html')
        kw.key_input('//*[@id="username"]', '18513087182')
        kw.key_input('//*[@id="password"]', '123456')
        kw.key_input('//*[@id="verify_code"]', '8888')
        kw.key_click('//*[@id="loginform"]/div/div[6]/a')
        kw.key_assert_text('/html/body/div[1]/div/div/div/div[2]/a[2]', '安全退出')
        # msg = kw.key_get_text('/html/body/div[10]/div/p')
        # assert msg == '登录成功'

        cookies = driver.get_cookies()
        with open('temps/cookies/cookies.json', 'w', encoding='utf-8') as f:
            json.dump(cookies, f)

    yield driver
    driver.quit()
