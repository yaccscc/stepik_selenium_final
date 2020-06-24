from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def get_product_cost(self):
        self.should_be_product_cost()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text

    def get_product_name(self):
        self.should_be_product_name()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def basket_cost_should_be_equals_to(self, equals_to: str):
        self.should_be_basket_cost()
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST).text
        assert basket_cost == equals_to, \
            f"Basket cost = {basket_cost} and {equals_to} are not equals"

    def product_added_to_basket_message_should_be_equals_to(self, equals_to: str):
        self.should_be_product_added_to_basket_message()
        product_added_message = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE).text
        assert product_added_message == equals_to, \
            f"Product added to basket = {product_added_message} and {equals_to} are not equals"

    def should_be_product_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Product added to basket message is not presented"

    def should_be_basket_cost(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST), \
            "Basket cost is not presented"

    def should_be_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), \
            "Product cost is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"
