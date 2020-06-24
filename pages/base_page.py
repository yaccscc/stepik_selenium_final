from typing import Union

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, url: str, browser: Union[webdriver.Chrome, webdriver.Firefox], timeout: int = 10):
        self.url = url
        self.browser = browser
        self.timeout = timeout

        self.browser.implicitly_wait(self.timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how: By, what: str):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
