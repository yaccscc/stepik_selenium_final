from typing import Union
import time

from selenium import webdriver

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser: Union[webdriver.Chrome, webdriver.Firefox]):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(link, browser)
    page.open()
    page.add_to_basket()
    page.basket_cost_should_be_equals_to(page.get_product_cost())
    page.product_added_to_basket_message_should_be_equals_to(page.get_product_name())
