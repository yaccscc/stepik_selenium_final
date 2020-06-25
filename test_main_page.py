from typing import Union

import pytest
from selenium import webdriver

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


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


@pytest.mark.dev
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    page = MainPage("http://selenium1py.pythonanywhere.com/", browser)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser.current_url, browser)
    basket_page.should_be_basket()
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_message()
