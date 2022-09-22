"""
@Filename:  cores/base
@Author:   lianpengwei
@Time:    2022/9/19 14:55
@Describe:  定义base层关键字
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import logging

from webdriver_helper import debugger

logger = logging.getLogger(__name__)


class KeyWord:

    def __init__(self, driver: WebDriver = None, request=None):
        """初始化driver"""
        self.request = request
        if driver:
            self.set_driver(driver)

    def set_driver(self, driver: WebDriver):
        """设置driver"""
        self.driver = driver
        driver.maximize_window()
        self.wait =WebDriverWait(driver, timeout=20, poll_frequency=0.1)

    def get_kw_method(self, key):
        """获取关键字方法"""
        f = getattr(self, f'key_{key}')
        if not f:
            raise AttributeError(f'不存在的关键字{key}')
        return f

    def key_driver_fixture(self, fixture_name):
        """
        使用pytest的fixture作为kw的driver
        :param fixture_name:
        :return:
        """
        driver = self.request.getfixturevalue(fixture_name)
        self.set_driver(driver)

    def key_get_url(self, url):
        self.driver.get(url)

    def find_element(self, *args):
        print('----------', *args)
        """
        封装元素定位方法, 自动使用显示等待
        :param args:
        :return:
        """
        logger.info(f'正在定位元素: {args}')
        # debugger(self.driver)
        el = self.wait.until(lambda _: self.driver.find_element(*args))
        logger.info('元素定位成功')
        return el

    def key_find_element(self, *args):
        """封装关键字查找元素方法"""
        logger.info(f'正在定位元素: {args}')
        # debugger(self.driver)
        el = self.wait.until(lambda _: self.driver.find_element(*args))
        logger.info('元素定位成功')
        return el

    def key_click(self, loc):
        """点击方法"""
        el: WebElement = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        el.click()

    def key_input(self, loc, value = None):
        """输入方法"""
        # debugger(self.driver)
        el: WebElement = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        el.clear()
        if value:
            el.send_keys(value)

    def key_get_text(self, loc):
        """获取元素文本内容"""
        el: WebElement = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        text = el.text.strip()
        return text

    def key_assert_text(self, loc, text):
        """断言文本"""
        # el: WebElement = self.find_element(By.XPATH, loc)
        # self.wait.until(lambda _: el.is_enabled())
        el_text = self.key_get_text(loc)
        # debugger(self.driver)
        logger.info(f'元素的文本是{el_text}')
        text = text.strip()
        logger.info(f'预期的文本是{text}')
        assert text == el_text

    def key_execute_js(self, loc, code):
        """执行js代码"""
        el: WebElement = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: el.is_enabled())
        self.driver.execute_script(code, el)

    def key_switch_frame(self, name):
        debugger(self.driver)
        self.driver.switch_to.frame(name)