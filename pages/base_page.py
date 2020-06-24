from typing import Union
import math

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
