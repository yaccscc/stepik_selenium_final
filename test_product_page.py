from typing import Union
import time

import pytest
from selenium import webdriver

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.long
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser: Union[webdriver.Chrome, webdriver.Firefox], link):
    page = ProductPage(link, browser)
    page.open()
    page.add_to_basket()
    page.basket_cost_should_be_equals_to(page.get_product_cost())
    page.product_added_to_basket_message_should_be_equals_to(page.get_product_name())


def test_guest_cant_see_success_message(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(link, browser)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(
        browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(link, browser)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(link, browser)
    page.open()
    page.add_to_basket()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_from_product_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(link, browser)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(link, browser)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser.current_url, browser)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(link, browser)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser.current_url, browser)
    basket_page.should_be_basket()
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_basket_message()
