from typing import Union

from selenium import webdriver

from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_should_see_login_link(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    page = MainPage("http://selenium1py.pythonanywhere.com/", browser)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    page = MainPage("http://selenium1py.pythonanywhere.com/", browser)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser.current_url, browser)
    login_page.should_be_login_page()
