from typing import Union

from selenium import webdriver


class BasePage:
    def __init__(self, url: str, browser: Union[webdriver.Chrome, webdriver.Firefox]):
        self.url = url
        self.browser = browser

    def open(self):
        self.browser.get(self.url)
